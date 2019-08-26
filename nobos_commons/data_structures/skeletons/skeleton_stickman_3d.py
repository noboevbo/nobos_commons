from nobos_commons.data_structures.skeletons.skeleton_stickman import SkeletonStickman
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints_3D import SkeletonStickmanJoints3D
from nobos_commons.data_structures.skeletons.skeleton_stickman_limbs_3d import SkeletonStickmanLimbs3D


class SkeletonStickman3D(SkeletonStickman):
    joints: SkeletonStickmanJoints3D = SkeletonStickmanJoints3D()
    limbs: SkeletonStickmanLimbs3D = SkeletonStickmanLimbs3D(joints)

    def __init__(self):
        """
        Override class attributes with instance attributes
        """
        super().__init__()
        self.joints: SkeletonStickmanJoints3D = SkeletonStickmanJoints3D()
        self.limbs: SkeletonStickmanLimbs3D = SkeletonStickmanLimbs3D(self.joints)
