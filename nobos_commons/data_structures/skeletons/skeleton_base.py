from typing import List, TypeVar, Generic, Any, Dict

import numpy as np

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

    def __init__(self):
        self.__joint_array = None

    def get_joint_array(self, use_cache=False, min_score=None) -> np.ndarray:
        if use_cache:
            if self.__joint_array is None:
                self.__joint_array = self.joints.to_numpy(min_score=min_score)
            return self.__joint_array
        return self.joints.to_numpy()

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

    def get_skeleton_config_dict(self) -> Dict[str, Dict[str, Any]]:
        limb_list = []
        joint_list = []
        for limb in self.limbs:
            limb_color = None
            if self.limb_colors[limb.num] is not None:
                limb_color = self.limb_colors[limb.num].hex
            limb_dict = limb.to_dict()
            limb_dict["color"] = limb_color
            limb_list.append(limb_dict)
        for joint in self.joints:
            joint_color = None
            if self.joint_colors[joint.num] is not None:
                joint_color = self.joint_colors[joint.num].hex
            joint_dict = joint.to_dict()
            joint_dict["color"] = joint_color
            joint_list.append(joint_dict)
        skeleton_config: Dict[str, Dict[str, Any]] = {"limbs": limb_list, "joints": joint_list}
        return skeleton_config
