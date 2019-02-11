from typing import List

from nobos_commons.data_structures.bounding_box import BoundingBox
from nobos_commons.data_structures.dimension import Vec3D, Vec2D
from nobos_commons.data_structures.humans_metadata.action import Action
from nobos_commons.data_structures.skeletons.skeleton_base import SkeletonBase
from nobos_commons.utils.bounding_box_helper import get_human_bounding_box_from_joints


class Human(object):
    __slots__ = ['uid', 'skeleton', 'action', 'frame_num', '_bounding_box', '_score']

    def __init__(self, uid: str = None, skeleton: SkeletonBase = None, bounding_box: BoundingBox = None,
                 action: Action = None, frame_nr: int = None):
        """
        Contains pose information about a human from within a image
        """
        self.uid = uid
        self.skeleton = skeleton
        self.action: Action = action
        self.frame_num: int = frame_nr
        self._bounding_box = bounding_box
        self._score = 0

    @property
    def joint_list(self) -> List[List[int]]:
        joint_list = []
        for joint in self.skeleton.joints:
            joint_list.append([joint.x, joint.y])
        return joint_list

    @property
    def score(self) -> float:
        if self._score == 0:
            self._score = self.skeleton.score
        return self._score

    @property
    def bounding_box(self) -> BoundingBox:
        if self._bounding_box is None:
            self._bounding_box = get_human_bounding_box_from_joints(self.skeleton.joints)
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box: BoundingBox):
        self._bounding_box = bounding_box


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
