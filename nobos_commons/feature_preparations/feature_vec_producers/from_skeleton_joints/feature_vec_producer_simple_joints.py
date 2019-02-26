from typing import Callable

import numpy as np
from nobos_commons.data_structures.dimension import ImageSize
from nobos_commons.data_structures.skeletons.skeleton_stickman import SkeletonStickman
from nobos_commons.feature_preparations.feature_vec_producers.from_skeleton_joints.feature_vec_joint_config import \
    get_joints_default
from nobos_commons.utils.human_surveyor import HumanSurveyor


class FeatureVecProducerSimpleJoints(object):
    def __init__(self, image_size: ImageSize, human_surveyor: HumanSurveyor = HumanSurveyor(),
                 get_joints_func: Callable = lambda skeleton: get_joints_default(skeleton),
                 skeleton: SkeletonStickman = SkeletonStickman(), with_score: bool = False):
        self.__image_size = image_size
        self.human_surveyor = human_surveyor
        self.get_joints_func: Callable = get_joints_func
        joints = self.get_joints_func(skeleton)
        self.num_joints = len(joints)
        self.with_score = with_score
        # We have 4 features for each combination of 2 joints and 3 features for each combination of 3 joints
        if self.with_score:
            self.feature_vec_length = int(3 * self.num_joints)
        else:
            self.feature_vec_length = int(2 * self.num_joints)

    def get_feature_vec(self, skeleton: SkeletonStickman) -> np.ndarray:
        """
        Returns the (unnormalized) feature vec
        :param skeleton:
        :return:
        """
        # human_height = self.human_surveyor.get_human_height(skeleton.limbs)
        joints = self.get_joints_func(skeleton)
        if self.with_score:
            feature_vec = np.zeros((len(joints), 3), dtype=np.float32)
            for idx, joint in enumerate(joints):
                feature_vec[idx][0] = joint.x / self.__image_size.width
                feature_vec[idx][1] = joint.y / self.__image_size.height
                feature_vec[idx][2] = joint.score
        else:
            feature_vec = np.zeros((len(joints), 2), dtype=np.float32)
            for idx, joint in enumerate(joints):
                feature_vec[idx][0] = joint.x / self.__image_size.width
                feature_vec[idx][1] = joint.y / self.__image_size.height

        return feature_vec
