from typing import TypeVar, Generic, Type

from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.joint_3d import Joint3D
from nobos_commons.data_structures.skeletons.skeleton_joints_base import SkeletonJointsBase

T = TypeVar('T', Joint2D, Joint3D)

class SkeletonStickmanJointsBase(SkeletonJointsBase[T], Generic[T]):
    def __init__(self, joint_class: Type[T]):
        """
        Implementation only works on Python 3.6+
        """
        self._nose: T = joint_class(num=0, name='nose')
        self._neck: T = joint_class(num=1, name='neck')
        self._right_shoulder: T = joint_class(num=2, name='right_shoulder')
        self._right_elbow: T = joint_class(num=3, name='right_elbow')
        self._right_wrist: T = joint_class(num=4, name='right_wrist')
        self._left_shoulder: T = joint_class(num=5, name='left_shoulder')
        self._left_elbow: T = joint_class(num=6, name='left_elbow')
        self._left_wrist: T = joint_class(num=7, name='left_wrist')
        self._right_hip: T = joint_class(num=8, name='right_hip')
        self._right_knee: T = joint_class(num=9, name='right_knee')
        self._right_ankle: T = joint_class(num=10, name='right_ankle')
        self._left_hip: T = joint_class(num=11, name='left_hip')
        self._left_knee: T = joint_class(num=12, name='left_knee')
        self._left_ankle: T = joint_class(num=13, name='left_ankle')
        self._right_eye: T = joint_class(num=14, name='right_eye')
        self._left_eye: T = joint_class(num=15, name='left_eye')
        self._right_ear: T = joint_class(num=16, name='right_ear')
        self._left_ear: T = joint_class(num=17, name='left_ear')
        self._hip_center: T = joint_class(num=18, name='hip_center')

    @property
    def nose(self) -> T:
        return self._nose

    @property
    def neck(self) -> T:
        return self._neck

    @property
    def right_shoulder(self) -> T:
        return self._right_shoulder

    @property
    def right_elbow(self) -> T:
        return self._right_elbow

    @property
    def right_wrist(self) -> T:
        return self._right_wrist

    @property
    def left_shoulder(self) -> T:
        return self._left_shoulder

    @property
    def left_elbow(self) -> T:
        return self._left_elbow

    @property
    def left_wrist(self) -> T:
        return self._left_wrist

    @property
    def right_hip(self) -> T:
        return self._right_hip

    @property
    def right_knee(self) -> T:
        return self._right_knee

    @property
    def right_ankle(self) -> T:
        return self._right_ankle

    @property
    def left_hip(self) -> T:
        return self._left_hip

    @property
    def left_knee(self) -> T:
        return self._left_knee

    @property
    def left_ankle(self) -> T:
        return self._left_ankle

    @property
    def right_eye(self) -> T:
        return self._right_eye

    @property
    def left_eye(self) -> T:
        return self._left_eye

    @property
    def right_ear(self) -> T:
        return self._right_ear

    @property
    def left_ear(self) -> T:
        return self._left_ear

    @property
    def hip_center(self) -> T:
        return self._hip_center
