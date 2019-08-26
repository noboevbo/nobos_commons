from typing import Dict, Any

import numpy as np

from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.joint_visibility import JointVisibility


class Joint3D(Joint2D):
    __slots__ = ['_num', '_name', 'x', 'y', 'z', 'score', 'visibility']

    def __init__(self, num: int = -1, name: str = None, x: int = 0, y: int = 0, z: int = 0, score: float = 0,
                 visibility: JointVisibility = JointVisibility.VISIBLE):
        """
        Data class for 2D joints
        :param num: The number of the joint in the skeleton configuration
        :param name: The name of the joint
        :param x: The X coordinate (row pixel in image)
        :param y: The Y coordinate (column pixel in image)
        :param score: The prediction score
        :param visibility: The visibility of the joint (Usually only used in datasets for training purpose)
        """
        super().__init__(num, name, x, y, score, visibility)
        self.z: int = z

    def copy_from(self, other: 'Joint3D', allow_different_num: bool = False, allow_different_name: bool = False):
        super().copy_from(other, allow_different_num, allow_different_name)
        self.z = other.z

    @property
    def is_set(self) -> bool:
        return super().is_set and self.z != 0

    def reset(self):
        """
        Sets the joint to the default (unset) state.
        """
        super().reset()
        self.z = 0

    # Serialization

    def to_dict(self):
        result = super().to_dict()
        result['z'] = self.z
        return result

    def to_numpy_position(self):
        return np.array([self.x, self.y, self.z])

    @staticmethod
    def from_dict(joint_3d_dict: Dict[str, Any]) -> 'Joint3D':
        return Joint3D(num=joint_3d_dict['num'],
                       name=joint_3d_dict['name'],
                       x=int(joint_3d_dict['x']),
                       y=int(joint_3d_dict['y']),
                       z=int(joint_3d_dict['z']),
                       score=float(joint_3d_dict['score']),
                       visibility=JointVisibility[joint_3d_dict['visibility']])

    def __repr__(self):
        return "num: '{}'; name: '{}'; x: '{}', y: '{}', z: '{}' score: '{}', visibility: '{}'".format(self.num,
                                                                                                       self.name,
                                                                                                       self.x, self.y,
                                                                                                       self.z,
                                                                                                       self.score,
                                                                                                       self.visibility)
