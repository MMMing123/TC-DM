# Ultralytics YOLO 🚀, AGPL-3.0 license

import cv2
import numpy as np
import onnxruntime as ort
from ultralytics import YOLO

CLASS_NAMES = {
    0: 'class_name1',
    1: 'class_name2',
    2: 'class_name3'
}


class YOLO11:
    """Optimized YOLOv11 object detection class"""

    def __init__(self, onnx_model="Resources/yolo11n.onnx", confidence_thres=0.7, iou_thres=0.6):
        self.onnx_model = onnx_model
        self.confidence_thres = confidence_thres
        self.iou_thres = iou_thres
        self.classes = CLASS_NAMES
        self.color_palette = np.random.uniform(0, 255, size=(len(self.classes), 3))

        # Initialize ONNX Runtime session
        self.session = self.initialize_onnx_session()

        # Get model input specifications
        model_inputs = self.session.get_inputs()
        self.input_shape = model_inputs[0].shape
        self.input_height = self.input_shape[2]
        self.input_width = self.input_shape[3]

    def initialize_onnx_session(self):
        """Initialize optimized ONNX Runtime session"""
        session_options = ort.SessionOptions()
        session_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        session_options.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL
        session_options.enable_cpu_mem_arena = True

        providers = ["CUDAExecutionProvider", "CPUExecutionProvider"] if ort.get_device() == "GPU" else [
            "CPUExecutionProvider"]

        return ort.InferenceSession(
            self.onnx_model,
            sess_options=session_options,
            providers=providers,
        )

    def preprocess(self, ir):
        """Optimized preprocessing function"""
        # Use model input dimensions directly to avoid unnecessary copying
        img = np.asarray(ir, dtype=np.float32) / 255.0
        img = img.transpose(2, 0, 1)[np.newaxis, ...]  # Complete transpose and dimension expansion in a single step
        return np.ascontiguousarray(img)

    def postprocess(self, output):
        """Optimized postprocessing function"""
        outputs = np.squeeze(output[0]).T
        max_scores = np.max(outputs[:, 4:], axis=1)
        valid_mask = max_scores >= self.confidence_thres

        if not np.any(valid_mask):
            return [0, 0, 640, 576], False

        outputs = outputs[valid_mask]
        class_ids = np.argmax(outputs[:, 4:], axis=1)

        # Use advanced indexing to get scores for corresponding classes
        scores = outputs[np.arange(len(outputs)), 4 + class_ids].astype(float)  # Ensure conversion to Python float

        # Filter non-target classes (class_id=0)
        person_mask = class_ids == 0
        if not np.any(person_mask):
            return [0, 0, 640, 576], False

        outputs = outputs[person_mask]
        scores = scores[person_mask]

        # Decode bounding boxes (vectorized operation)
        boxes = outputs[:, :4].copy()  # Create copy to avoid modifying original data
        boxes[:, 0] -= boxes[:, 2] / 2  # left
        boxes[:, 1] -= boxes[:, 3] / 2  # top
        boxes[:, 2] = boxes[:, 0] + boxes[:, 2]  # right
        boxes[:, 3] = boxes[:, 1] + boxes[:, 3]  # bottom

        # Convert coordinates to integers and ensure data type
        boxes = boxes.astype(np.int32)
        scores = scores.tolist()  # Convert to Python native float list

        # Use OpenCV's NMS
        indices = cv2.dnn.NMSBoxes(boxes.tolist(), scores,  # Note: directly using scores list
                                   self.confidence_thres, self.iou_thres)

        if len(indices) == 0:
            return [0, 0, 640, 576], False

        best_idx = indices[0]
        return boxes[best_idx].tolist(), True

    def run(self, ir):
        """Optimized inference pipeline"""
        img_data = self.preprocess(ir)
        outputs = self.session.run(None, {self.session.get_inputs()[0].name: img_data})
        return self.postprocess(outputs)