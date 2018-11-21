from typing import Dict

from nobos_commons.data_structures.human import Joint2D
from nobos_commons.data_structures.skeletons.skeleton_joints_base import SkeletonJointsBase


class SkeletonStickmanJoints(SkeletonJointsBase):
    __dict__: Dict[str, Joint2D]
    __slots__ = [
        'nose'
        'neck'
        'right_shoulder'
        'right_elbow'
        'right_wrist'
        'left_shoulder'
        'left_elbow'
        'left_wrist'
        'right_hip'
        'right_knee'
        'right_ankle'
        'left_hip'
        'left_knee'
        'left_ankle'
        'right_eye'
        'left_eye'
        'right_ear'
        'left_ear'
        'hip_center'
    ]

    def __init__(self):
        """
        Implementation only works on Python 3.6+
        """
        self.nose: Joint2D = None
        self.neck: Joint2D = None
        self.right_shoulder: Joint2D = None
        self.right_elbow: Joint2D = None
        self.right_wrist: Joint2D = None
        self.left_shoulder: Joint2D = None
        self.left_elbow: Joint2D = None
        self.left_wrist: Joint2D = None
        self.right_hip: Joint2D = None
        self.right_knee: Joint2D = None
        self.right_ankle: Joint2D = None
        self.left_hip: Joint2D = None
        self.left_knee: Joint2D = None
        self.left_ankle: Joint2D = None
        self.right_eye: Joint2D = None
        self.left_eye: Joint2D = None
        self.right_ear: Joint2D = None
        self.left_ear: Joint2D = None
        self.hip_center: Joint2D = None
