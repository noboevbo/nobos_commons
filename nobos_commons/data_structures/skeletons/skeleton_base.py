from typing import List, TypeVar, Generic, Any, Dict

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

    # Serialization

    def to_dict(self) -> Dict[str, Any]:
        return {
            'joints': self.joints.to_dict()
        }

    def copy_from_dict(self, in_dict: Dict[str, Any]):
        self.joints.copy_from_dict(in_dict['joints'])
