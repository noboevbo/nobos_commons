from typing import List, Dict

from nobos_commons.data_structures.bounding_box import BoundingBox
from nobos_commons.data_structures.dimension import Vec3D, Vec2D
import numpy as np

from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.limb_2d import Limb2D
from nobos_commons.data_structures.skeletons.skeleton_base import SkeletonBase


class HumanPoseResult(object):
    __slots__ = ['skeleton', 'score', 'heatmaps', '__num_limbs', 'uid', 'bounding_box']

    @property
    def num_limbs(self) -> int:
        self.__num_limbs = 0
        for limb in self.skeleton.limbs:
            if limb.is_set:
                self.__num_limbs += 1
        return self.__num_limbs

    @property
    def joint_list(self) -> List[List[int]]:
        joint_list = []
        for joint in self.skeleton.joints:
            joint_list.append([joint.x, joint.y])
        return joint_list

    def __init__(self, skeleton: SkeletonBase, score: float, uid: str = None, bounding_box: BoundingBox = None,
                 heatmaps: np.ndarray = None):
        """
        Contains pose information about a human from within a image
        :param joints: The joints in the skeleton of the human
        :param limbs: The limbs in the skeleton of the human # TODO is ugly because not existing limbs will be placed in this list with None ...
        :param score: The combined score of joints and limbs of the given human
        """
        self.skeleton = skeleton
        self.score = score # TODO: Score should be calculated on the fly..
        self.uid = uid
        self.bounding_box = bounding_box # TODO: Should be calculated from skeleton if none
        self.heatmaps = heatmaps

        self.__num_limbs = 0 # TODO: rename to num_perceived_limbs or so


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
        """
        Contains Metadata of a human
        :param hip_center: The center of the hip of the human (3D)
        :param direction_point: A point in the direction of the humans body (3D)
        :param camera_hip_distance: The distance of the humans hip to the cameras center (in meters)
        """
        self.hip_center = hip_center
        self.direction_point = direction_point
        self.camera_hip_distance = camera_hip_distance
