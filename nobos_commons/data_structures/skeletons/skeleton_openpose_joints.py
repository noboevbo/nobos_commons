from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.skeleton_joints_base import SkeletonJointsBase


class SkeletonOpenPoseJoints(SkeletonJointsBase):
    def __init__(self):
        """
        Implementation only works on Python 3.6+
        """
        self._nose: Joint2D = Joint2D(num=0, name='nose')
        self._neck: Joint2D = Joint2D(num=1, name='neck')
        self._right_shoulder: Joint2D = Joint2D(num=2, name='right_shoulder')
        self._right_elbow: Joint2D = Joint2D(num=3, name='right_elbow')
        self._right_wrist: Joint2D = Joint2D(num=4, name='right_wrist')
        self._left_shoulder: Joint2D = Joint2D(num=5, name='left_shoulder')
        self._left_elbow: Joint2D = Joint2D(num=6, name='left_elbow')
        self._left_wrist: Joint2D = Joint2D(num=7, name='left_wrist')
        self._right_hip: Joint2D = Joint2D(num=8, name='right_hip')
        self._right_knee: Joint2D = Joint2D(num=9, name='right_knee')
        self._right_ankle: Joint2D = Joint2D(num=10, name='right_ankle')
        self._left_hip: Joint2D = Joint2D(num=11, name='left_hip')
        self._left_knee: Joint2D = Joint2D(num=12, name='left_knee')
        self._left_ankle: Joint2D = Joint2D(num=13, name='left_ankle')
        self._right_eye: Joint2D = Joint2D(num=14, name='right_eye')
        self._left_eye: Joint2D = Joint2D(num=15, name='left_eye')
        self._right_ear: Joint2D = Joint2D(num=16, name='right_ear')
        self._left_ear: Joint2D = Joint2D(num=17, name='left_ear')

    @property
    def nose(self) -> Joint2D:
        return self._nose

    @property
    def neck(self) -> Joint2D:
        return self._neck

    @property
    def right_shoulder(self) -> Joint2D:
        return self._right_shoulder

    @property
    def right_elbow(self) -> Joint2D:
        return self._right_elbow

    @property
    def right_wrist(self) -> Joint2D:
        return self._right_wrist

    @property
    def left_shoulder(self) -> Joint2D:
        return self._left_shoulder

    @property
    def left_elbow(self) -> Joint2D:
        return self._left_elbow

    @property
    def left_wrist(self) -> Joint2D:
        return self._left_wrist

    @property
    def right_hip(self) -> Joint2D:
        return self._right_hip

    @property
    def right_knee(self) -> Joint2D:
        return self._right_knee

    @property
    def right_ankle(self) -> Joint2D:
        return self._right_ankle

    @property
    def left_hip(self) -> Joint2D:
        return self._left_hip

    @property
    def left_knee(self) -> Joint2D:
        return self._left_knee

    @property
    def left_ankle(self) -> Joint2D:
        return self._left_ankle

    @property
    def right_eye(self) -> Joint2D:
        return self._right_eye

    @property
    def left_eye(self) -> Joint2D:
        return self._left_eye

    @property
    def right_ear(self) -> Joint2D:
        return self._right_ear

    @property
    def left_ear(self) -> Joint2D:
        return self._left_ear
