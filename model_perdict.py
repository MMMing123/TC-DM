import torch
import pyk4a
import onnxruntime
from pyk4a import K4AException

from Modification import wheel_xyz, wheel_Confidence, wheel_Confidence_sort
from pyskl.apis import inference_recognizer, init_recognizer
import mmcv
from collections import deque
from anchor import post_process
import cv2
import time
import numpy as np

from yolov11 import YOLO11  # YOLOv11 human detection model


# Convert pixel coordinates to world coordinates
def pixel2world(x, y, z):
    worldX = (x - cx) * z / fx
    worldY = (y - cy) * z / fy
    return worldX, worldY


# Calculate the mean depth value ignoring zero pixels
def ca_mean(depth):
    if (depth != 0).sum() == 0:  # If entire depth map is zero
        mean = 0
    else:
        mean = depth.sum() / (depth != 0).sum()  # Calculate mean excluding zeros
    return mean


# Initialize Azure Kinect camera
k4a = pyk4a.PyK4A(
    config=pyk4a.Config(
        color_resolution=pyk4a.ColorResolution.RES_720P,
        depth_mode=pyk4a.DepthMode.NFOV_UNBINNED,
        camera_fps=pyk4a.FPS.FPS_30,
        synchronized_images_only=True,
    )
)

# Mapping of joint IDs to human body part names
joint_id_to_name = {
    0: 'left_ear',
    1: 'right_ear',
    2: 'left_eye',
    3: 'right_eye',
    4: 'nose',
    5: 'neck',
    6: 'chest',
    7: 'hip',
    8: 'left_hip',
    9: 'right_hip',
    10: 'left_wrist',
    11: 'right_wrist',
    12: 'left_elbow',
    13: 'right_elbow',
    14: 'left_shoulder',
    15: 'right_shoulder',
}

# Skeleton connection definitions (bone links)
connections = [
    (0, 2), (2, 4),  # Left ear -> left eye -> nose
    (1, 3), (3, 4),  # Right ear -> right eye -> nose
    (4, 5), (5, 6),  # Nose -> neck -> chest
    (5, 14), (5, 15),  # Neck to shoulders
    (14, 12), (15, 13),  # Shoulders to elbows
    (12, 10), (13, 11),  # Elbows to wrists
    (6, 7),  # Chest to hip
    (7, 8), (7, 9),  # Hip to legs
]

# Fixed camera intrinsic parameters
cx = 318.5131530761719  # Optical center X
cy = 338.0367431640625  # Optical center Y
fx = 504.7893371582031  # Focal length X
fy = 504.9712829589844  # Focal length Y


# Detect person in IR image using YOLOv11
def detect_person_in_ir(ir_image):
    return ir_ob.run(ir_image)


# Colorize depth image for visualization
def colorize(image, clipping_range=(None, None)):
    if clipping_range[0] is not None:
        image[image < clipping_range[0]] = clipping_range[0]  # Clip low values
    if clipping_range[1] is not None:
        image[image > clipping_range[1]] = clipping_range[1]  # Clip high values
    normalized = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)  # Normalize to 0-255
    return cv2.applyColorMap(cv2.convertScaleAbs(normalized, alpha=1), cv2.COLORMAP_HSV)  # Apply color map


# Initialize global variables
prev_time = time.time()  # Timestamp of previous frame
fps = 0  # Current FPS value
fps_history = deque(maxlen=30)  # FPS history for smoothing
BUFFER_SIZE = 30  # Action recognition buffer size
SMOOTH_SIZE = 5  # Smoothing buffer size
FRAME_SKIP = 1  # Process every 2nd frame (0,1,0,1,...)
frame_counter = 0  # Frame counter
skeleton_buffer = deque(maxlen=BUFFER_SIZE)  # Stores 3D skeleton data
prediction_buffer = deque(maxlen=SMOOTH_SIZE)  # Stores action predictions
detection_buffer = deque(maxlen=SMOOTH_SIZE)  # Stores object detection results
action_history = deque(maxlen=10)  # Stores action label history

# State preservation variables
last_keypoints = None  # Last detected keypoints
last_world_coords = None  # Last 3D world coordinates
last_action_label = "Normal Driving"  # Last detected action label
last_action_score = 0  # Confidence score of last action
last_all_scores = []  # All action confidence scores
last_person_detected = False  # Person detection status
last_bbox = [0, 0, 640, 576]  # Last bounding box [x1,y1,x2,y2]
last_detections = []  # Last object detections [x1,y1,x2,y2,conf,cls_id,label]

# Global thresholds
CONFIDENCE_THRESHOLD = 0.65  # Minimum confidence for action recognition
ACTION_STABILITY_THRESHOLD = 3  # Minimum occurrence for stable action detection

# Initialize action recognition model
config = mmcv.Config.fromfile('work_dirs/150_8_2/j.py')
config.data.test.pipeline = [x for x in config.data.test.pipeline if x['type'] != 'DecompressPose']
device2 = 'cuda:0' if torch.cuda.is_available() else 'cpu'
action_model = init_recognizer(config, 'work_dirs/150_8_2/best_top1_acc_epoch_36.pth', device2)

# Load action labels
label_map = [x.strip() for x in open('Resources/3D.txt').readlines()]
skeleton_labels_lower = [label.lower() for label in label_map]  # Lowercase labels for matching

### Inference engines ###
providers = ['CUDAExecutionProvider', "CPUExecutionProvider"]
## 1. Pose estimation ONNX model
inf_session = onnxruntime.InferenceSession(r'Resources/a2j.onnx', providers=providers)
## 2. Human detection (YOLOv11)
ir_ob = YOLO11()
## 3. Object detection for actions (YOLOv5)
action_detect_model = torch.hub.load('ultralytics/yolov5', 'custom', path='Resources/yolov5.pt')
device3 = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
action_detect_model.to(device3)

# Action detection label mapping
action_detect_labels = ['drinking and eating', 'drinking and eating', 'mobile use', 'smoking']


## Display mode: 0 = Depth + Skeleton, 1 = Skeleton only
def update(Display=0):
    # Access global state variables
    global last_action_score, last_action_label, \
        last_all_scores, last_bbox, frame_counter, last_world_coords, \
        last_detections, prev_time, last_keypoints, fps, k4a

    display_action = "Normal Driving"  # Default display action

    # Ensure camera is running
    if not k4a.opened:
        try:
            k4a.start()
        except K4AException as e:
            if k4a.opened:
                k4a.stop()
            raise e

    # Use last frame's data as fallback
    PixKeypointD = last_keypoints
    world_coords = last_world_coords
    action_score = last_action_score
    action_label = last_action_label

    # Get camera capture
    capture = k4a.get_capture()
    depth_image = capture.depth  # Depth frame

    # Prepare visualization image
    if Display == 0:
        depth_image_primary = depth_image.copy()
        depth_image_primary = colorize(depth_image_primary, (None, 5000))  # Colorize depth (0-5000mm)
    else:
        depth_image_primary = np.ones((576, 640, 3), dtype=np.uint8) * 255  # White background

    # Process IR image
    ir_image = capture.ir
    ir_image = cv2.convertScaleAbs(ir_image, alpha=0.05)  # Scale to 8-bit
    ir_image = np.dstack([ir_image, ir_image, ir_image])  # Convert to 3-channel

    # Human detection
    bbox, person_detected = detect_person_in_ir(ir_image)
    if person_detected:
        last_bbox = bbox
        last_person_detected = True
    else:
        last_person_detected = False
        bbox = last_bbox  # Use last valid bbox
        person_detected = False
        # Clear skeleton data on processing frames
        if frame_counter % (FRAME_SKIP + 1) == 0:
            last_keypoints = None
            if skeleton_buffer: skeleton_buffer.clear()

    # Process every Nth frame (based on FRAME_SKIP)
    if frame_counter % (FRAME_SKIP + 1) == 0 and person_detected:
        # Crop depth image to detection area
        new_Xmin = max(bbox[0], 0)
        new_Ymin = max(bbox[1], 0)
        new_Xmax = min(bbox[2], 640 - 1)
        new_Ymax = min(bbox[3], 576 - 1)
        depth_image = depth_image[int(new_Ymin):int(new_Ymax), int(new_Xmin):int(new_Xmax)]

        # Resize and normalize depth patch
        depth_image = cv2.resize(depth_image, (288, 288), interpolation=cv2.INTER_NEAREST)
        depth_image = np.asarray(depth_image, dtype=np.float32)
        std = 1
        mean = ca_mean(depth_image)  # Calculate mean depth
        depth_image[depth_image != 0] = (depth_image[depth_image != 0] - mean) / std  # Normalize
        depth_image = depth_image[np.newaxis, np.newaxis, :, :]  # Add batch/channel dims

        ## Pose estimation inference
        with torch.no_grad():
            # Run ONNX model
            a = inf_session.run(['y1', 'y2', 'y3'], {"input": depth_image})
            # Convert outputs to CUDA tensors
            y1, y2, y3 = [torch.from_numpy(x).to(device3) for x in a]

        # Post-process pose predictions
        post = post_process(shape=[288 // 16, 288 // 16], stride=16, P_h=None, P_w=None)
        PixKeypointD = post((y1, y2, y3))
        PixKeypointD = torch.squeeze(PixKeypointD).cpu().numpy()  # [16,3]

        # Map keypoints back to original image coordinates
        PixKeypointD[:, 0] = PixKeypointD[:, 0] * (new_Ymax - new_Ymin) / 288 + new_Ymin
        PixKeypointD[:, 1] = PixKeypointD[:, 1] * (new_Xmax - new_Xmin) / 288 + new_Xmin

        # Convert to 3D world coordinates
        world_coords = []
        for i in range(16):
            x = int(PixKeypointD[i][1])
            y = int(PixKeypointD[i][0])
            z = int(PixKeypointD[i][2])
            # Clamp coordinates to image bounds
            x = max(0, min(x, 640 - 1))
            y = max(0, min(y, 576 - 1))
            world_x, world_y = pixel2world(x, y, z)
            world_coords.append([world_x, world_y, z])

        # Add to skeleton buffer
        skeleton_buffer.append(np.array(world_coords))

        # Action recognition when buffer is full
        if len(skeleton_buffer) == BUFFER_SIZE:
            # Create annotation structure for action model
            fake_anno = dict(
                frame_dir='',
                label=-1,
                img_shape=(576, 640),
                original_shape=(576, 640),
                start_index=0,
                modality='Skeleton',
                total_frames=BUFFER_SIZE)

            # Format skeleton sequence [1, T, 16, 3]
            keypoint = np.zeros((1, BUFFER_SIZE, 16, 3), dtype=np.float32)
            for i, coords in enumerate(skeleton_buffer):
                keypoint[0, i] = coords
            fake_anno['keypoint'] = keypoint
            fake_anno['total_frames'] = BUFFER_SIZE

            # Run action recognition
            results = inference_recognizer(action_model, fake_anno)

            # Initialize action scores
            all_scores = [(i, 0.0) for i in range(len(label_map))]
            for idx, score in results:
                all_scores[idx] = (idx, score)

            prediction_buffer.append(all_scores)  # Add to prediction buffer

            # Smooth scores over time window
            smoothed_scores = [(i, 0.0) for i in range(len(label_map))]
            if len(prediction_buffer) == SMOOTH_SIZE:
                for i in range(len(label_map)):
                    avg_score = sum(pred[i][1] for pred in prediction_buffer) / SMOOTH_SIZE
                    smoothed_scores[i] = (i, avg_score)

                # Get top predicted action
                sorted_smooth = sorted(smoothed_scores, key=lambda x: x[1], reverse=True)
                action_score = sorted_smooth[0][1]
                predicted_action = label_map[sorted_smooth[0][0]]
                predicted_action_lower = predicted_action.lower()

                ## Object detection for secondary verification
                with torch.no_grad():
                    detect_results = action_detect_model(ir_image)
                detect_scores = {label: 0.0 for label in action_detect_labels}

                # Process detections
                last_detections = []
                for det in detect_results.pred[0]:
                    if len(det):
                        x1, y1, x2, y2, conf, cls_id = det.cpu().numpy()
                        cls_id = int(cls_id)
                        conf = float(conf)
                        if cls_id < len(action_detect_labels):
                            label = action_detect_labels[cls_id]
                            detect_scores[label] = conf
                            if conf > 0.3:  # Confidence threshold
                                last_detections.append([x1, y1, x2, y2, conf, cls_id, label])

                detection_buffer.append(detect_scores)  # Add to buffer

                # Smooth detection scores
                smoothed_detect_scores = {label: 0.0 for label in action_detect_labels}
                if len(detection_buffer) == SMOOTH_SIZE:
                    for label in action_detect_labels:
                        smoothed_detect_scores[label] = sum(
                            frame[label] for frame in detection_buffer) / SMOOTH_SIZE
                else:
                    smoothed_detect_scores = detect_scores

                # Find highest confidence object
                max_detect_score = 0.0
                max_detect_label = None
                for label, score in smoothed_detect_scores.items():
                    if score > max_detect_score:
                        max_detect_score = score
                        max_detect_label = label

                ## Decision logic ##
                # Priority to object detection
                if max_detect_label and max_detect_score > 0.3:
                    action_label = max_detect_label
                    action_score = max_detect_score
                # Ignore if both methods agree
                elif predicted_action_lower == max_detect_label:
                    action_label = "Normal Driving"
                    action_score = 0
                # Use pose prediction if unique and confident
                elif predicted_action_lower not in action_detect_labels and action_score >= CONFIDENCE_THRESHOLD:
                    action_label = predicted_action
                else:
                    action_label = "Normal Driving"

                action_history.append(action_label)  # Update history
                all_scores = smoothed_scores

            # Update global state
            last_keypoints = PixKeypointD
            last_world_coords = world_coords
            last_action_label = action_label
            last_action_score = action_score
            last_all_scores = all_scores

            ## Draw skeleton on visualization image ##
            joint_points = {i: (int(PixKeypointD[i, 1]), int(PixKeypointD[i, 0])) for i in range(16)}
            # Draw connections (bones)
            for start_joint_id, end_joint_id in connections:
                start_point = joint_points[start_joint_id]
                end_point = joint_points[end_joint_id]
                cv2.line(depth_image_primary, start_point, end_point, (0, 255, 0), 2)
            # Draw joints
            for i in range(16):
                x, y = PixKeypointD[i][1], PixKeypointD[i][0]
                cv2.circle(depth_image_primary, (int(x), int(y)), radius=2, color=(43, 43, 43), thickness=20)

    # Non-processing frame: draw last skeleton if available
    elif person_detected and last_person_detected and last_keypoints is not None:
        joint_points = {i: (int(last_keypoints[i, 1]), int(last_keypoints[i, 0])) for i in range(16)}
        for start_joint_id, end_joint_id in connections:
            start_point = joint_points[start_joint_id]
            end_point = joint_points[end_joint_id]
            cv2.line(depth_image_primary, start_point, end_point, (0, 255, 0), 2)
        for i in range(16):
            x, y = last_keypoints[i][1], last_keypoints[i][0]
            cv2.circle(depth_image_primary, (int(x), int(y)), radius=2, color=(43, 43, 43), thickness=20)

    # Calculate FPS
    current_time = time.time()
    time_diff = current_time - prev_time
    prev_time = current_time
    if time_diff > 0:
        current_fps = 1 / time_diff
        fps_history.append(current_fps)
        fps = sum(fps_history) / len(fps_history)  # Smoothed FPS

    # Prepare display image
    display_scale = 1
    display_image = cv2.resize(depth_image_primary,
                               (int(depth_image_primary.shape[1] * display_scale),
                                int(depth_image_primary.shape[0] * display_scale)))

    # Display FPS counter
    cv2.putText(display_image, f"FPS: {int(fps)} (Skip: {FRAME_SKIP + 1})",
                (int(10 * display_scale), int(30 * display_scale)),
                cv2.FONT_HERSHEY_SIMPLEX,
                display_scale, (0, 255, 0), 2)

    # Action stabilization logic
    if last_person_detected and len(skeleton_buffer) == BUFFER_SIZE:
        # Count occurrences in action history
        action_counts = {}
        for action in action_history:
            action_counts[action] = action_counts.get(action, 0) + 1
        # Find most frequent action
        max_count = 0
        most_frequent_action = "Normal Driving"
        for action, count in action_counts.items():
            if count > max_count:
                max_count = count
                most_frequent_action = action
        # Apply stability threshold
        display_action = most_frequent_action if max_count >= ACTION_STABILITY_THRESHOLD else "Normal Driving"
    elif not last_person_detected:
        cv2.putText(display_image, "No Person Detected",
                    (int(10 * display_scale), int(70 * display_scale)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    display_scale, (0, 0, 255), 2)

    frame_counter += 1

    ## Format action scores for output ##
    # Initialize score array [action_id, confidence]
    all_scores_my = [[i, 0] for i in range(13)]  # 13 action classes

    # Map detected action to score array
    if display_action == "calling":
        all_scores_my[0][1] = action_score
    elif display_action == "dive":
        all_scores_my[1][1] = action_score
    elif display_action in ["drinking", "drinking and eating"]:
        all_scores_my[2][1] = action_score
    elif display_action == "eating":
        all_scores_my[3][1] = action_score
    elif display_action == "get":
        all_scores_my[4][1] = action_score
    elif display_action == "operate":
        all_scores_my[5][1] = action_score
    elif display_action == "mobile use":
        all_scores_my[6][1] = action_score
    elif display_action == "pick":
        all_scores_my[7][1] = action_score
    elif display_action == "smoking":
        all_scores_my[8][1] = action_score
    elif display_action == "take":
        all_scores_my[9][1] = action_score
    elif display_action == "tilt":
        all_scores_my[10][1] = action_score
    elif display_action == "Normal Driving":
        all_scores_my[11][1] = action_score
    elif display_action == "No Person Detected":
        all_scores_my[12][1] = 1  # Special case

    # Default to "Normal Driving" if no action detected
    if action_score == 0:
        all_scores_my[11][1] = 1

    # Sort scores descending
    all_scores_sort_my = sorted(all_scores_my, key=lambda x: x[1], reverse=True)

    ## Steering wheel position correction ##
    if all_scores_my and person_detected and PixKeypointD is not None:
        nose_x, nose_y = PixKeypointD[4][1], PixKeypointD[4][0]  # Nose position
        all_scores_my = wheel_Confidence(nose_x, nose_y, all_scores_my, PixKeypointD[:, :2])
        all_scores_sort_my = wheel_Confidence_sort(nose_x, nose_y, all_scores_sort_my, PixKeypointD[:, :2])

    return display_image, all_scores_my, all_scores_sort_my, world_coords


# Get raw depth frame with FPS overlay
def org_depth():
    global fps, prev_time, cx, cy, fx, fy
    cx, cy, fx, fy = Camera_internal_reference_set()  # Load camera intrinsics

    capture = k4a.get_capture()
    depth_image = capture.depth
    org_depth_image = depth_image.copy()  # Raw depth
    depth_image_primary = colorize(depth_image.copy(), (None, 5000))  # Colorized

    # Calculate FPS
    current_time = time.time()
    time_diff = current_time - prev_time
    prev_time = current_time
    if time_diff > 0:
        fps = 1 / time_diff

    # Prepare display image
    display_scale = 1
    display_image = cv2.resize(depth_image_primary,
                               (int(depth_image_primary.shape[1] * display_scale),
                                int(depth_image_primary.shape[0] * display_scale)))

    # Draw FPS counter
    cv2.putText(display_image, f"FPS: {int(fps)}",
                (int(10 * display_scale), int(30 * display_scale)),
                cv2.FONT_HERSHEY_SIMPLEX,
                display_scale, (0, 255, 0), 2)

    return display_image, org_depth_image  # Colorized and raw depth


# Load camera intrinsic parameters from file
def Camera_internal_reference_set():
    with open('Resources/Camera_internal_reference.txt', 'r') as file:
        params = [float(line.strip()) for line in file.readlines()[:4]]
    cx, cy, fx, fy = params
    return cx, cy, fx, fy


# Draw steering wheel overlay on image
def draw_wheel(img):
    u, v = wheel_xyz()  # Get wheel center position
    center = (int(u), int(v))
    # Draw blue ellipse representing steering wheel
    cv2.ellipse(
        img,
        center,
        (15, 8),  # Major/minor axes
        -30,  # Rotation angle (tilted 30 degrees right)
        0,  # Start angle
        360,  # End angle (full ellipse)
        (255, 0, 0),  # Blue color
        2  # Thickness
    )
    return img