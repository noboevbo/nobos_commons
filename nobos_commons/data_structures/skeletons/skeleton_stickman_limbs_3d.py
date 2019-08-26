from nobos_commons.data_structures.skeletons.limb_3d import Limb3D
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints_3D import SkeletonStickmanJoints3D
from nobos_commons.data_structures.skeletons.skeleton_stickman_limbs_base import SkeletonStickmanLimbsBase


class SkeletonStickmanLimbs3D(SkeletonStickmanLimbsBase):
    def __init__(self, skeleton_joints: SkeletonStickmanJoints3D):
        super().__init__(skeleton_joints, Limb3D)
