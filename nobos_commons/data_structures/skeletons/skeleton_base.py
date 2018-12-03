from typing import List

from nobos_commons.data_structures.color import Color
from nobos_commons.data_structures.skeletons.skeleton_joints_base import SkeletonJointsBase
from nobos_commons.data_structures.skeletons.skeleton_limbs_base import SkeletonLimbsBase


class SkeletonBase(object):
    """
    The abstract skeleton class, needs to be implemented by concrete instances.
    """
    joints: SkeletonJointsBase
    limbs: SkeletonLimbsBase
    limb_colors: List[Color]
    joint_colors: List[Color]

    def auto_set_limbs_from_joints(self):
        """
        Sets limb to set and its score based on the joints values in the skeleton.
        """

        for limb in self.limbs:
            if limb.joint_to.is_set and limb.joint_from.is_set:
                limb.score = (limb.joint_from.score + limb.joint_to.score) / 2
