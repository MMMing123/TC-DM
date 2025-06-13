import math

def wheel_xyz():
    """Read steering wheel coordinates from file"""
    with open('Resources/wheel.txt', 'r') as file:
        x, y = 0, 0
        i = 0
        lines = file.readlines()
        for line in lines:
            if (i == 0):
                x = float(line.strip())
            elif (i == 1):
                y = float(line.strip())
            elif (i == 2):
                continue
            i = i + 1
    return x, y

# Reset confidence based on steering wheel, must be unsorted confidence, set the 10th "forward lean" to (10,1) and others to 0, similarly set the 2nd "backward lean"
def wheel_Confidence(u, v, Confidence, keypoints):
    """Get steering wheel distance and set thresholds"""
    wheel_x, wheel_y = wheel_xyz()
    with open('Resources/Threshold.txt', 'r', encoding='utf-8') as file:
        i = 0
        lines = file.readlines()
        for line in lines:
            if (i == 0):
                wheel_Threshold = float(line.strip())
            elif (i == 1):
                dive_value = float(line.strip())
            elif (i == 2):
                tilt_value = float(line.strip())
            i = i + 1
    with open('Resources/wheel.txt', 'r') as file:
        Driving_position = 0
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i == 2:

                Driving_position = float(line.strip())



                break
    Difference_value = u-wheel_x

    """Adjust for forward/backward leaning angles"""
    TF_is_driver_leaning_back_0 = is_driver_leaning_back(keypoints,dive_value,Driving_position)
    TF_is_driver_leaning_forward_0 = is_driver_tilt(keypoints, tilt_value,Driving_position)
    if Driving_position == 1:
        if TF_is_driver_leaning_back_0:
            TF_is_driver_leaning_forward =  True
        else: TF_is_driver_leaning_forward = False
        if TF_is_driver_leaning_forward_0:
            TF_is_driver_leaning_back = True
        else: TF_is_driver_leaning_back = False
    else:
        TF_is_driver_leaning_back = TF_is_driver_leaning_back_0
        TF_is_driver_leaning_forward = TF_is_driver_leaning_forward_0
    if TF_is_driver_leaning_back:
        for i in range(12):
            if i == 1:
                Confidence[i] = (1, 1.00)
            else:
                Confidence[i] = (i, 0.00)
    elif TF_is_driver_leaning_forward:
        for i in range(12):
            if i == 10:
                Confidence[i] = (1, 1.00)
            else:
                Confidence[i] = (i, 0.00)

    """Adjust for steering wheel distance"""
    if Driving_position == 0:
        if Difference_value > wheel_Threshold :
            for i in range(12):
                if i == 10:
                    Confidence[i] = (10, 1.00)
                else:
                    Confidence[i] = (i, 0.00)

    else:
        if Difference_value < wheel_Threshold :
            for i in range(12):
                if i == 10:
                    Confidence[i] = (10, 1.00)
                else:
                    Confidence[i] = (i, 0.00)

    return Confidence

## Sorted version
def wheel_Confidence_sort(u, v, Confidence, keypoints):
    """Get steering wheel distance and set thresholds"""
    wheel_x, wheel_y = wheel_xyz()
    with open('Resources/Threshold.txt', 'r', encoding='utf-8') as file:
        i = 0
        lines = file.readlines()
        for line in lines:
            if (i == 0):
                wheel_Threshold = float(line.strip())
            elif (i == 1):
                dive_value = float(line.strip())
            elif (i == 2):
                tilt_value = float(line.strip())
            i = i + 1
    with open('Resources/wheel.txt', 'r') as file:
        Driving_position = 0
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i == 2:
                Driving_position = float(line.strip())
                break
    Difference_value = u - wheel_x

    """Adjust for forward/backward leaning angles"""
    TF_is_driver_leaning_back_0 = is_driver_leaning_back(keypoints,dive_value,Driving_position)
    # This forward tilt might be backward tilt because it is judged only based on the body Angle
    TF_is_driver_leaning_forward_0 = is_driver_tilt(keypoints, tilt_value,Driving_position)
    if TF_is_driver_leaning_back_0: ## If it is leaning backward
        TF_is_driver_leaning_forward_0 = False ##Then it must not be leaning forward
    if Driving_position == 1:
        if TF_is_driver_leaning_back_0:
            TF_is_driver_leaning_forward =  True
        else: TF_is_driver_leaning_forward = False
        if TF_is_driver_leaning_forward_0:
            TF_is_driver_leaning_back = True
        else: TF_is_driver_leaning_back = False
    else:
        TF_is_driver_leaning_back = TF_is_driver_leaning_back_0
        TF_is_driver_leaning_forward = TF_is_driver_leaning_forward_0
    if TF_is_driver_leaning_back:
        for i in range(12):
            if i == 0:
                Confidence[i] = (1, 1.00)
            else:
                Confidence[i] = (i, 0.00)
    elif TF_is_driver_leaning_forward:
        for i in range(12):
            if i == 0:
                Confidence[i] = (10, 1.00)
            else:
                Confidence[i] = (i, 0.00)
    """Adjust for steering wheel"""
    if Driving_position ==0:
        if Difference_value >= wheel_Threshold:
            for i in range(12):
                if i == 0:
                    Confidence[i] = (10, 1.00)
                else:
                    Confidence[i] = (i, 0.00)
    else:

        if Difference_value <= wheel_Threshold:
            for i in range(12):
                if i == 0:
                    Confidence[i] = (10, 1.00)
                else:
                    Confidence[i] = (i, 0.00)
    return Confidence

def is_driver_leaning_back(keypoints, threshold_angle=15.0,wheel_xyz_Driving_position=0):
    """
    Determine if the driver is leaning back
    :param keypoints: Human keypoints coordinates array, shape [16, 2]
    :param threshold_angle: Backward lean judgment threshold angle (default 15.0)
    :return: bool, True for leaning back, False for normal
    """
    # Get neck and hip keypoints coordinates
    neck = keypoints[5]  # ID5 is neck
    chest = keypoints[6]  # ID6 is hip (originally commented as chest, fixed)

    dx = neck[0] - chest[0]  # Horizontal difference
    dy = neck[1] - chest[1]  # Vertical difference

    # When neck is below or at same level as hip, unlikely
    if dy >= 0:
        return False

    # Calculate angle between torso line and vertical direction
    try:
        angle_rad = math.atan2(dx, -dy)  # Use negative dy (y-axis downward)
        angle_deg = math.degrees(angle_rad)
    except ZeroDivisionError:
        angle_deg = 90.0  # Handle completely horizontal case

    # Current angle

    angle_current = 90 - abs(angle_deg)



    return angle_current > threshold_angle



import math


def is_driver_tilt(keypoints, threshold_angle=15.0, wheel_xyz_Driving_position=0):
    """
    Determine if the driver is leaning forward (面向图片右侧)
    :param keypoints: Human keypoints coordinates array, shape [16, 2]
    :param threshold_angle: Forward lean judgment threshold angle (default 15.0)
    :return: bool, True for leaning forward, False for normal
    """
    # Get neck and hip keypoints coordinates
    neck = keypoints[5]  # ID5 is neck [x, y]
    chest = keypoints[6]  # ID6 is hip [x, y]


    dx = neck[0] - chest[0]
    dy = neck[1] - chest[1]


    if dy < 0:

        angle_deg = math.degrees(math.atan2(dx, -dy))
    elif dy > 0:
        angle_deg = math.degrees(math.atan2(dx, dy))
    else:
        angle_deg = 90.0 if dx != 0 else 0.0


    angle_deg = 90-abs(angle_deg)
    # 判断前倾：角度为正且超过阈值
    return angle_deg > threshold_angle

