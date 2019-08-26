from typing import TypeVar, Type, Generic

from nobos_commons.data_structures.skeletons.limb_2d import Limb2D
from nobos_commons.data_structures.skeletons.limb_3d import Limb3D
from nobos_commons.data_structures.skeletons.skeleton_limbs_base import SkeletonLimbsBase
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints import SkeletonStickmanJoints

T = TypeVar('T', Limb2D, Limb3D)


class SkeletonStickmanLimbsBase(SkeletonLimbsBase, Generic[T]):
    def __init__(self, skeleton_joints: SkeletonStickmanJoints, limb_class: Type[T]):
        self._neck_to_right_shoulder: T = limb_class(num=0,
                                                     joint_from=skeleton_joints.neck,
                                                     joint_to=skeleton_joints.right_shoulder)
        self._neck_to_left_shoulder: T = limb_class(num=1,
                                                    joint_from=skeleton_joints.neck,
                                                    joint_to=skeleton_joints.left_shoulder)
        self._right_shoulder_to_right_elbow: T = limb_class(num=2,
                                                            joint_from=skeleton_joints.right_shoulder,
                                                            joint_to=skeleton_joints.right_elbow)
        self._right_elbow_to_right_wrist: T = limb_class(num=3,
                                                         joint_from=skeleton_joints.right_elbow,
                                                         joint_to=skeleton_joints.right_wrist)
        self._left_shoulder_to_left_elbow: T = limb_class(num=4,
                                                          joint_from=skeleton_joints.left_shoulder,
                                                          joint_to=skeleton_joints.left_elbow)
        self._left_elbow_to_left_wrist: T = limb_class(num=5,
                                                       joint_from=skeleton_joints.left_elbow,
                                                       joint_to=skeleton_joints.left_wrist)
        self._neck_to_hip_center: T = limb_class(num=6,
                                                 joint_from=skeleton_joints.neck,
                                                 joint_to=skeleton_joints.hip_center)
        self._hip_center_to_right_hip: T = limb_class(num=7,
                                                      joint_from=skeleton_joints.hip_center,
                                                      joint_to=skeleton_joints.right_hip)
        self._right_hip_to_right_knee: T = limb_class(num=8,
                                                      joint_from=skeleton_joints.right_hip,
                                                      joint_to=skeleton_joints.right_knee)
        self._right_knee_to_right_ankle: T = limb_class(num=9,
                                                        joint_from=skeleton_joints.right_knee,
                                                        joint_to=skeleton_joints.right_ankle)
        self._hip_center_to_left_hip: T = limb_class(num=10,
                                                     joint_from=skeleton_joints.hip_center,
                                                     joint_to=skeleton_joints.left_hip)
        self._left_hip_to_left_knee: T = limb_class(num=11,
                                                    joint_from=skeleton_joints.left_hip,
                                                    joint_to=skeleton_joints.left_knee)
        self._left_knee_to_left_ankle: T = limb_class(num=12,
                                                      joint_from=skeleton_joints.left_knee,
                                                      joint_to=skeleton_joints.left_ankle)
        self._neck_to_nose: T = limb_class(num=13,
                                           joint_from=skeleton_joints.neck,
                                           joint_to=skeleton_joints.nose)
        self._nose_to_right_eye: T = limb_class(num=14,
                                                joint_from=skeleton_joints.nose,
                                                joint_to=skeleton_joints.right_eye)
        self._right_eye_to_right_ear: T = limb_class(num=15,
                                                     joint_from=skeleton_joints.right_eye,
                                                     joint_to=skeleton_joints.right_ear)
        self._nose_to_left_eye: T = limb_class(num=16,
                                               joint_from=skeleton_joints.nose,
                                               joint_to=skeleton_joints.left_eye)
        self._left_eye_to_left_ear: T = limb_class(num=17,
                                                   joint_from=skeleton_joints.left_eye,
                                                   joint_to=skeleton_joints.left_ear)
        self._right_shoulder_to_right_ear: T = limb_class(num=18,
                                                          joint_from=skeleton_joints.right_shoulder,
                                                          joint_to=skeleton_joints.right_ear)
        self._left_shoulder_to_left_ear: T = limb_class(num=19,
                                                        joint_from=skeleton_joints.left_shoulder,
                                                        joint_to=skeleton_joints.left_ear)

    @property
    def neck_to_right_shoulder(self) -> T:
        return self._neck_to_right_shoulder

    @property
    def neck_to_left_shoulder(self) -> T:
        return self._neck_to_left_shoulder

    @property
    def right_shoulder_to_right_elbow(self) -> T:
        return self._right_shoulder_to_right_elbow

    @property
    def right_elbow_to_right_wrist(self) -> T:
        return self._right_elbow_to_right_wrist

    @property
    def left_shoulder_to_left_elbow(self) -> T:
        return self._left_shoulder_to_left_elbow

    @property
    def left_elbow_to_left_wrist(self) -> T:
        return self._left_elbow_to_left_wrist

    @property
    def neck_to_hip_center(self) -> T:
        return self._neck_to_hip_center

    @property
    def hip_center_to_right_hip(self) -> T:
        return self._hip_center_to_right_hip

    @property
    def right_hip_to_right_knee(self) -> T:
        return self._right_hip_to_right_knee

    @property
    def right_knee_to_right_ankle(self) -> T:
        return self._right_knee_to_right_ankle

    @property
    def hip_center_to_left_hip(self) -> T:
        return self._hip_center_to_left_hip

    @property
    def left_hip_to_left_knee(self) -> T:
        return self._left_hip_to_left_knee

    @property
    def left_knee_to_left_ankle(self) -> T:
        return self._left_knee_to_left_ankle

    @property
    def neck_to_nose(self) -> T:
        return self._neck_to_nose

    @property
    def nose_to_right_eye(self) -> T:
        return self._nose_to_right_eye

    @property
    def right_eye_to_right_ear(self) -> T:
        return self._right_eye_to_right_ear

    @property
    def nose_to_left_eye(self) -> T:
        return self._nose_to_left_eye

    @property
    def left_eye_to_left_ear(self) -> T:
        return self._left_eye_to_left_ear

    @property
    def right_shoulder_to_right_ear(self) -> T:
        return self._right_shoulder_to_right_ear

    @property
    def left_shoulder_to_left_ear(self) -> T:
        return self._left_shoulder_to_left_ear
