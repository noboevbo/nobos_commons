from typing import List

from nobos_commons.data_structures.color import Color
from nobos_commons.data_structures.skeletons.skeleton_joints_base import SkeletonJointsBase
from nobos_commons.data_structures.skeletons.skeleton_limbs_base import SkeletonLimbsBase


class SkeletonMeta(type):
    _joints: SkeletonJointsBase
    _limbs: SkeletonLimbsBase

    @property
    def joints(cls) -> SkeletonJointsBase:
        return cls._joints

    @property
    def limbs(cls) -> SkeletonLimbsBase:
        return cls._limbs


class SkeletonBase(metaclass=SkeletonMeta):
    """
    The abstract skeleton class, needs to be implemented by concrete instances.
    """
    _joints: SkeletonJointsBase
    _limbs: SkeletonLimbsBase

    limb_colors: List[Color]
    joint_colors: List[Color]

    @property
    def joints(self) -> SkeletonJointsBase:
        return self._joints

    @property
    def limbs(self) -> SkeletonLimbsBase:
        return self._limbs

    def auto_set_limbs_from_joints(self):
        """
        Sets limb to set and its score based on the joints values in the skeleton.
        """

        for limb in self.limbs:
            if limb.joint_to.is_set and limb.joint_from.is_set:
                limb.score = (limb.joint_from.score + limb.joint_to.score) / 2
