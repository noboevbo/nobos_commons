from nobos_commons.data_structures.skeletons.limb_2d import Limb2D
from nobos_commons.data_structures.skeletons.skeleton_limbs_base import SkeletonLimbsBase
from nobos_commons.data_structures.skeletons.skeleton_jhmdb_joints import SkeletonJhmdbJoints


class SkeletonJhmdbLimbs(SkeletonLimbsBase):
    def __init__(self, skeleton_joints: SkeletonJhmdbJoints):
        self._neck_to_head: Limb2D = Limb2D(num=1,
                                            joint_from=skeleton_joints.neck,
                                            joint_to=skeleton_joints.head)
        self._neck_to_belly: Limb2D = Limb2D(num=2,
                                             joint_from=skeleton_joints.neck,
                                             joint_to=skeleton_joints.belly)
        self._neck_to_right_shoulder: Limb2D = Limb2D(num=3,
                                                      joint_from=skeleton_joints.neck,
                                                      joint_to=skeleton_joints.right_shoulder)
        self._neck_to_left_shoulder: Limb2D = Limb2D(num=4,
                                                     joint_from=skeleton_joints.neck,
                                                     joint_to=skeleton_joints.left_shoulder)
        self._right_shoulder_to_right_elbow: Limb2D = Limb2D(num=5,
                                                             joint_from=skeleton_joints.right_shoulder,
                                                             joint_to=skeleton_joints.right_elbow)
        self._left_shoulder_to_left_elbow: Limb2D = Limb2D(num=6,
                                                           joint_from=skeleton_joints.left_shoulder,
                                                           joint_to=skeleton_joints.left_elbow)
        self._right_elbow_to_right_wrist: Limb2D = Limb2D(num=7,
                                                          joint_from=skeleton_joints.right_elbow,
                                                          joint_to=skeleton_joints.right_wrist)
        self._left_elbow_to_left_wrist: Limb2D = Limb2D(num=8,
                                                        joint_from=skeleton_joints.left_elbow,
                                                        joint_to=skeleton_joints.left_wrist)
        self._belly_to_right_hip: Limb2D = Limb2D(num=9,
                                                  joint_from=skeleton_joints.belly,
                                                  joint_to=skeleton_joints.right_hip)
        self._belly_to_left_hip: Limb2D = Limb2D(num=10,
                                                 joint_from=skeleton_joints.belly,
                                                 joint_to=skeleton_joints.left_hip)
        self._right_hip_to_right_knee: Limb2D = Limb2D(num=11,
                                                       joint_from=skeleton_joints.right_hip,
                                                       joint_to=skeleton_joints.right_knee)
        self._left_hip_to_left_knee: Limb2D = Limb2D(num=12,
                                                     joint_from=skeleton_joints.left_hip,
                                                     joint_to=skeleton_joints.left_knee)
        self._right_knee_to_right_ankle: Limb2D = Limb2D(num=13,
                                                         joint_from=skeleton_joints.right_knee,
                                                         joint_to=skeleton_joints.right_ankle)
        self._left_knee_to_left_ankle: Limb2D = Limb2D(num=14,
                                                       joint_from=skeleton_joints.left_knee,
                                                       joint_to=skeleton_joints.left_ankle)

    @property
    def neck_to_head(self) -> Limb2D:
        return self._neck_to_head

    @property
    def neck_to_belly(self) -> Limb2D:
        return self._neck_to_belly

    @property
    def neck_to_right_shoulder(self) -> Limb2D:
        return self._neck_to_right_shoulder

    @property
    def neck_to_left_shoulder(self) -> Limb2D:
        return self._neck_to_left_shoulder

    @property
    def right_shoulder_to_right_elbow(self) -> Limb2D:
        return self._right_shoulder_to_right_elbow

    @property
    def left_shoulder_to_left_elbow(self) -> Limb2D:
        return self._left_shoulder_to_left_elbow

    @property
    def right_elbow_to_right_wrist(self) -> Limb2D:
        return self._right_elbow_to_right_wrist

    @property
    def left_elbow_to_left_wrist(self) -> Limb2D:
        return self._left_elbow_to_left_wrist

    @property
    def belly_to_right_hip(self) -> Limb2D:
        return self._belly_to_right_hip

    @property
    def belly_to_left_hip(self) -> Limb2D:
        return self._belly_to_left_hip

    @property
    def right_hip_to_right_knee(self) -> Limb2D:
        return self._right_hip_to_right_knee

    @property
    def left_hip_to_left_knee(self) -> Limb2D:
        return self._left_hip_to_left_knee

    @property
    def right_knee_to_right_ankle(self) -> Limb2D:
        return self._right_knee_to_right_ankle

    @property
    def left_knee_to_left_ankle(self) -> Limb2D:
        return self._left_knee_to_left_ankle
