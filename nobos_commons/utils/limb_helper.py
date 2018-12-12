from typing import Dict, Type

from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.limb_2d import Limb2D
from nobos_commons.data_structures.skeletons.skeleton_base import SkeletonBase
from nobos_commons.data_structures.skeletons.skeleton_stickman_joints import SkeletonStickmanJoints
from nobos_commons.data_structures.skeletons.skeleton_stickman_limbs import SkeletonStickmanLimbs
from nobos_commons.utils.joint_helper import get_euclidean_distance_joint2d


def get_limb_length(limb: Limb2D) -> float:
    return get_euclidean_distance_joint2d(limb.joint_from, limb.joint_to)


def get_limbs_from_joints(joints: Dict[int, Joint2D], skeleton_type: Type[SkeletonBase]) -> SkeletonStickmanLimbs:
    """
    TODO: Remove this? Replaced by auto_set_limbs in skeleton.
    :param joints:
    :param skeleton_type:
    :return:
    """
    limbs: SkeletonStickmanLimbs = SkeletonStickmanLimbs(SkeletonStickmanJoints())
    # TODO: scores?
    for limb in skeleton_type.limbs:
        joint_from = joints[limb.joint_from.num]
        joint_to = joints[limb.joint_to.num]
        if not joint_from.is_set or not joint_to.is_set:
            limbs[limb.num].reset()
            continue
        limbs[limb.num].joint_from.copy_from(joint_from)
        limbs[limb.num].joint_to.copy_from(joint_to)
    return limbs
