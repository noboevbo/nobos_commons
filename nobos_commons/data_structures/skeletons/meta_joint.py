from typing import Dict, Any

import numpy as np

from nobos_commons.data_structures.dimension import Vec3D
from nobos_commons.data_structures.math_structures import Quaternion
from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.joint_visibility import JointVisibility


class MetaJoint(object):
    __slots__ = ['name', 'x', 'y', 'z', 'rotation', 'direction_vec', 'score', 'visibility']

    def __init__(self, num: float = -1, name: str = None, x: float = 0, y: float = 0, z: float = 0, score: float = 0,
                 visibility: JointVisibility = JointVisibility.VISIBLE, rotation: Quaternion = None, direction_vec: Vec3D = None):
        """
        Data class for 2D joints
        :param num: The number of the joint in the skeleton configuration
        :param name: The name of the joint
        :param x: The X coordinate (row pixel in image)
        :param y: The Y coordinate (column pixel in image)
        :param score: The prediction score
        :param visibility: The visibility of the joint (Usually only used in datasets for training purpose)
        :param rotation: The rotation of the joint as a quaternion
        """
        self.name: str = name
        self.x: float = x
        self.y: float = y
        self.score: float = score
        self.visibility: JointVisibility = visibility
        self.z: float = z
        self.rotation: Quaternion = rotation
        self.direction_vec: Vec3D = direction_vec

