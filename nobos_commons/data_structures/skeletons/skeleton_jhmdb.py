from nobos_commons.data_structures.color import Color
from nobos_commons.data_structures.skeletons.skeleton_base import SkeletonBase
from nobos_commons.data_structures.skeletons.skeleton_jhmdb_joints import SkeletonJhmdbJoints
from nobos_commons.data_structures.skeletons.skeleton_jhmdb_limbs import SkeletonJhmdbLimbs


class SkeletonJhmdb(SkeletonBase):
    joints: SkeletonJhmdbJoints = SkeletonJhmdbJoints()
    limbs: SkeletonJhmdbLimbs = SkeletonJhmdbLimbs(joints)

    def __init__(self):
        """
        Override class attributes with instance attributes
        """
        super().__init__()
        self.joints: SkeletonJhmdbJoints = SkeletonJhmdbJoints()
        self.limbs: SkeletonJhmdbLimbs = SkeletonJhmdbLimbs(self.joints)

    joint_colors = [
        Color(r=0, g=0, b=0),  # Nose
        Color(r=0, g=0, b=0),  # LEye
        Color(r=0, g=0, b=0),  # REye
        Color(r=0, g=0, b=0),  # LEar
        Color(r=0, g=0, b=0),  # REar
        Color(r=0, g=0, b=0),  # LShoulder
        Color(r=0, g=0, b=0),  # RShoulder
        Color(r=0, g=0, b=0),  # LElbow
        Color(r=0, g=0, b=0),  # RElbow
        Color(r=0, g=0, b=0),  # LWrist
        Color(r=0, g=0, b=0),  # RWrist
        Color(r=0, g=0, b=0),  # LHip
        Color(r=0, g=0, b=0),  # RHip
        Color(r=0, g=0, b=0),  # LKnee
        Color(r=0, g=0, b=0),  # RKnee
        Color(r=0, g=0, b=0),  # LAnkle
        Color(r=0, g=0, b=0),  # RAnkle
    ]

    limb_colors = [
        Color(r=255, g=255, b=255),  # nose_to_left_eye
        Color(r=255, g=255, b=255),  # nose_to_right_eye
        Color(r=255, g=255, b=255),  # left_eye_to_left_ear
        Color(r=255, g=255, b=255),  # right_eye_to_right_ear
        Color(r=255, g=255, b=255),  # left_ear_to_left_shoulder
        Color(r=255, g=255, b=255),  # right_ear_to_right_shoulder
        Color(r=255, g=255, b=255),  # left_shoulder_to_left_elbow
        Color(r=255, g=255, b=255),  # right_shoulder_to_right_elbow
        Color(r=255, g=255, b=255),  # left_elbow_to_left_wrist
        Color(r=255, g=255, b=255),  # right_elbow_to_right_wrist
        Color(r=255, g=255, b=255),  # left_shoulder_to_left_hip
        Color(r=255, g=255, b=255),  # right_shoulder_to_right_hip
        Color(r=255, g=255, b=255),  # left_hip_to_left_knee
        Color(r=255, g=255, b=255),  # right_hip_to_right_knee
        Color(r=255, g=255, b=255),  # left_knee_to_left_ankle
        Color(r=255, g=255, b=255),  # right_knee_to_right_ankle
    ]
