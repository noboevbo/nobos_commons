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

    @property
    def score(self) -> float:
        score = 0
        for joint in self.joints:
            score += joint.score
        return score / len(self.joints)

    # Serialization

    def to_dict(self) -> Dict[str, Any]:
        return {
            'joints': self.joints.to_dict()
        }

    def copy_from_dict(self, in_dict: Dict[str, Any]):
        self.joints.copy_from_dict(in_dict['joints'])

    def get_limb_config_dict(self) -> Dict[str, Dict[str, Any]]:
        limb_dict: Dict[str, Dict[str, Any]] = {}
        for limb in self.limbs:
            limb_color = None
            if self.limb_colors[limb.num] is not None:
                limb_color = self.limb_colors[limb.num].hex
            limb_dict[limb.name] = {
                "color": limb_color,
                "joint_from": limb.joint_from.to_dict(),
                "joint_to": limb.joint_to.to_dict()
            }
        return limb_dict
