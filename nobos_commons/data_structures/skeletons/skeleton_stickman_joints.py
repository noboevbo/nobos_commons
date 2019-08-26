from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.skeleton_joints_base import SkeletonJointsBase
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints_base import SkeletonStickmanJointsBase


class SkeletonStickmanJoints(SkeletonStickmanJointsBase):
    def __init__(self):
        """
        Implementation only works on Python 3.6+
        """
        super().__init__(Joint2D)
