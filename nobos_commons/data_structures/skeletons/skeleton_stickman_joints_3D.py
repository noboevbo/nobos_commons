from nobos_commons.data_structures.skeletons.joint_3d import Joint3D
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints_base import SkeletonStickmanJointsBase


class SkeletonStickmanJoints3D(SkeletonStickmanJointsBase[Joint3D]):
    def __init__(self):
        """
        Implementation only works on Python 3.6+
        """
        super().__init__(Joint3D)
