from typing import List

from nobos_commons.data_structures.bounding_box import BoundingBox
from nobos_commons.data_structures.human import Human
from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.limb_2d import Limb2D


class ImageContent(object):
    __slots__ = ['humans', 'objects', 'straying_joints', 'straying_limbs']

    def __init__(self,
                 humans: List[Human] = [],
                 objects: List[BoundingBox] = [],
                 straying_joints: List[Joint2D] = [],
                 straying_limbs: List[Limb2D] = []
                 ):
        """
        Contains the content in a image observed by algorithm(s)
        """
        self.humans = humans
        # TODO: Objects should be more than a bounding box, the currently also include human bbs, how to distinguish?
        self.objects = objects
        self.straying_joints = straying_joints
        self.straying_limbs = straying_limbs
