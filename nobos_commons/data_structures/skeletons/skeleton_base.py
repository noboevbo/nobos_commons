from collections import OrderedDict
from typing import List

from nobos_commons.data_structures.color import Color
from nobos_commons.data_structures.skeletons.skeleton_joints_base import SkeletonJointsBase
from nobos_commons.data_structures.skeletons.skeleton_limbs_base import SkeletonLimbsBase


class SkeletonBase:
    joints: SkeletonJointsBase
    limbs: SkeletonLimbsBase
    limb_colors: List[Color]
    joint_colors: List[Color]
    # @property
    # def joints(self) -> SkeletonJointsBase:
    #     raise NotImplementedError
    #
    # @property
    # def limbs(self) -> SkeletonLimbsBase:
    #     raise NotImplementedError
    #
    # @property
    # def limb_colors(self) -> List[Color]:
    #     raise NotImplementedError
    #
    # @property
    # def joint_colors(self) -> List[Color]:
    #     raise NotImplementedError

    # def get_joint_name_by_id(self, joint_id):
    #     return list(self.joints.items())[joint_id][0]
