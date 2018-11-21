from nobos_commons.data_structures.human import Limb2D
from nobos_commons.data_structures.simple_base_data_class import SimpleBaseDataClass


class SkeletonStickmanLimbs(SimpleBaseDataClass):
    __slots__ = [
        'neck_to_right_shoulder'
        'neck_to_left_shoulder'
        'right_shoulder_to_right_elbow'
        'right_elbow_to_right_wrist'
        'left_shoulder_to_left_elbow'
        'left_elbow_to_left_wrist'
        'neck_to_hip_center'
        'hip_center_to_right_hip'
        'right_hip_to_right_knee'
        'right_knee_to_right_ankle'
        'hip_center_to_left_hip'
        'left_hip_to_left_knee'
        'left_knee_to_left_ankle'
        'neck_to_nose'
        'nose_to_right_eye'
        'right_eye_to_right_ear'
        'nose_to_left_eye'
        'left_eye_to_left_ear'
        'right_shoulder_to_right_ear'
        'left_shoulder_to_left_ear'
    ]

    def __init__(self):
        self.neck_to_right_shoulder: Limb2D = None
        self.neck_to_left_shoulder:Limb2D = None
        self.right_shoulder_to_right_elbow: Limb2D = None
        self.right_elbow_to_right_wrist: Limb2D = None
        self.left_shoulder_to_left_elbow: Limb2D = None
        self.left_elbow_to_left_wrist: Limb2D = None
        self.neck_to_hip_center: Limb2D = None
        self.hip_center_to_right_hip: Limb2D = None
        self.right_hip_to_right_knee: Limb2D = None
        self.right_knee_to_right_ankle: Limb2D = None
        self.hip_center_to_left_hip: Limb2D = None
        self.left_hip_to_left_knee: Limb2D = None
        self.left_knee_to_left_ankle: Limb2D = None
        self.neck_to_nose: Limb2D = None
        self.nose_to_right_eye: Limb2D = None
        self.right_eye_to_right_ear: Limb2D = None
        self.nose_to_left_eye: Limb2D = None
        self.left_eye_to_left_ear: Limb2D = None
        self.right_shoulder_to_right_ear: Limb2D = None
        self.left_shoulder_to_left_ear: Limb2D = None
