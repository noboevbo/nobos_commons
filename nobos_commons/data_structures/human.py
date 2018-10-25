from typing import List, Dict

from nobos_commons.data_structures.bounding_box import BoundingBox
from nobos_commons.data_structures.dimension import Vec3D, Vec2D
import numpy as np


class Joint2D(object):
    __slots__ = ['num', 'name', 'x', 'y', 'score', 'id']

    @property
    def coordinates(self):
        return [self.x, self.y]

    def __init__(self, num: int, x: int, y: int, score: float):
        """
        Data class for 2D joints
        :param num: The number of the joint in the skeleton configuration
        :param name: The name of the joint
        :param x: The X coordinate (row pixel in image)
        :param y: The Y coordinate (column pixel in image)
        :param score: The prediction score
        :param id: A unique id of the joint TODO: ?
        """
        self.num = num
        self.x = x
        self.y = y
        self.score = score


class Limb2D(object):
    __slots__ = ['num', 'joint_from', 'joint_to', 'score', 'matched_score']

    def __init__(self, num: int, joint_from: Joint2D, joint_to: Joint2D, score: float, matched_score: float):
        """

        :param num: The number of the limb in the skeleton configuration
        :param joint_from: The joint from which the limb goes
        :param joint_to: The joint to which the limb goes
        :param score: The score of the limb
        :param matched_score: The matched score of the limbs and the joints combined
        """
        self.num = num
        self.joint_from = joint_from
        self.joint_to = joint_to
        self.score = score
        self.matched_score = matched_score


class HumanPoseResult(object):
    __slots__ = ['joints', 'limbs', 'heatmaps', 'score', '__num_limbs', 'uid', 'bounding_box']

    @property
    def num_limbs(self) -> int:
        self.__num_limbs = 0
        for limb in self.limbs:
            if limb is not None:
                self.__num_limbs += 1
        return self.__num_limbs

    @property
    def joint_list(self) -> List[List[int]]:
        joint_list = []
        for joint in self.joints:
            joint_list.append([joint.x, joint.y])
        return joint_list

    def __init__(self, joints: List[Joint2D], limbs: List[Limb2D], score: float, uid: str = None, bounding_box: BoundingBox = None,
                 heatmaps: np.ndarray = None):
        """
        Contains pose information about a human from within a image
        :param joints: The joints in the skeleton of the human
        :param limbs: The limbs in the skeleton of the human # TODO is ugly because not existing limbs will be placed in this list with None ...
        :param score: The combined score of joints and limbs of the given human
        """
        self.joints = joints
        self.limbs = limbs
        self.score = score
        self.uid = uid
        self.bounding_box = bounding_box
        self.heatmaps = heatmaps

        self.__num_limbs = 0


class ImageContentHumans(object):
    __slots__ = ['img_path', 'humans', 'straying_joints', 'straying_limbs']

    def __init__(self, humans: List[HumanPoseResult] = [], straying_joints: Dict[int, List[Joint2D]] = {}, straying_limbs: Dict[int, List[Limb2D]] = {}):
        """
        Contains all human poses recognized in the given image
        :param img_path: The filepath of the image
        :param humans: The human poses contained in the image
        :param straying_joints: Joints which are recognized but not mapped to a human
        :param straying_limbs: Limbs which are recognized but not mapped to a human
        """
        self.humans = humans
        self.straying_joints = straying_joints
        self.straying_limbs = straying_limbs


class HumanMetadata(object):
    __slots__ = ['hip_center', 'direction_point', 'camera_hip_distance']

    def __init__(self, hip_center: Vec3D[float], direction_point: Vec2D[float], camera_hip_distance: Vec3D[float]):
        self.hip_center = hip_center
        self.direction_point = direction_point
        self.camera_hip_distance = camera_hip_distance
