from nobos_commons.data_structures.skeletons.limb_2d import Limb2D
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints import SkeletonStickmanJoints
from nobos_commons.data_structures.skeletons.skeleton_stickman_limbs_base import SkeletonStickmanLimbsBase


class SkeletonStickmanLimbs(SkeletonStickmanLimbsBase):
    def __init__(self, skeleton_joints: SkeletonStickmanJoints):
        super().__init__(skeleton_joints, Limb2D)
