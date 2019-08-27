from typing import Callable

import numpy as np
from nobos_commons.data_structures.dimension import ImageSize
from nobos_commons.data_structures.skeletons.skeleton_stickman_3d import SkeletonStickman3D
from nobos_commons.feature_preparations.feature_vec_producers.from_skeleton_joints.feature_vec_joint_config import \
    get_joints_default
from nobos_commons.utils.human_surveyor import HumanSurveyor


class FeatureVecProducerEhpi3D(object):
    def __init__(self, image_size: ImageSize, human_surveyor: HumanSurveyor = HumanSurveyor(),
                 get_joints_func: Callable = lambda skeleton: get_joints_default(skeleton),
                 skeleton: SkeletonStickman3D = SkeletonStickman3D()):
        self.__image_size = image_size
        self.human_surveyor = human_surveyor
        self.get_joints_func: Callable = get_joints_func
        joints = self.get_joints_func(skeleton)
        self.num_joints = len(joints)
        # We have 4 features for each combination of 2 joints and 3 features for each combination of 3 joints
        self.feature_vec_length = int(3 * self.num_joints)

    def get_feature_vec(self, skeleton: SkeletonStickman3D) -> np.ndarray:
        """
        Returns the (unnormalized) feature vec
        :param skeleton:
        :return:
        """
        # human_height = self.human_surveyor.get_human_height(skeleton.limbs)
        joints = self.get_joints_func(skeleton)
        feature_vec = np.zeros((len(joints), 3), dtype=np.float32)
        for idx, joint in enumerate(joints):
            if joint.score < 0.4:
                feature_vec[idx][0] = 0
                feature_vec[idx][1] = 0
                feature_vec[idx][2] = 0
            else:
                feature_vec[idx][0] = joint.x
                feature_vec[idx][1] = joint.y
                feature_vec[idx][2] = joint.z

        return feature_vec

