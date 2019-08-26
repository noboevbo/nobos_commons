from typing import List, Dict, Any, TypeVar, Generic

import numpy as np

from nobos_commons.data_structures.base_iterable_property_class import BaseIterablePropertyClass
from nobos_commons.data_structures.skeletons.joint_2d import Joint2D
from nobos_commons.data_structures.skeletons.joint_3d import Joint3D

T = TypeVar('T', Joint2D, Joint3D)


class SkeletonJointsBase(BaseIterablePropertyClass[T], Generic[T]):
    __dict__: Dict[str, T]

    @property
    def names(self) -> List[str]:
        names = []
        for key in self.__dict__.keys():
            names.append(key[1:])
        return names

    def copy_from_list(self, joint_list: List[T]):
        """
        Takes joints from a lists and copies their parameters to the SkeletonJoints. It does not allow for duplicated
        joints in the list.
        :param joint_list: A list of Ts which parameters should be set in this skeleton_joints
        """
        added_joint_nums: List[int] = []
        for joint in joint_list:
            assert joint.num not in added_joint_nums, "Duplicated joint num {0} found!".format(joint.num)
            assert joint.num < len(self), "joint number {0} is not available in this skeleton.".format(joint.num)
            added_joint_nums.append(joint.num)
            self[joint.num].copy_from(joint)

    def copy_from_other(self, other: 'SkeletonJointsBase'):
        """
        Copies the values from the other SkeletonJoints
        :param other: other skeleton joints, must be of the same type
        """
        assert type(self) == type(other), 'Can\'t copy values from another type!'
        for joint in other:
            self[joint.name].copy_from(joint)

    def num_joints_set(self):
        """
        Returns the number of joints which are actually parameterized.
        :return: The number of joints which are actually parameterized.
        """
        count = 0
        for joint in self:
            if joint.is_set:
                count += 1
        return count

    # Serialization

    def to_numpy(self, min_score: float = None, include_score: bool = False) -> np.ndarray:
        """
        Returns the joints concatenated in a one dimensional vector.
        :return: 1-dim numpy array (float32)
        """
        is_3D = type(self[0]) is Joint3D
        step_size = 3 if is_3D else 2
        if include_score:
            step_size += 1
        num_coordinates = len(self) * step_size
        numpy_array = np.zeros(num_coordinates, dtype=np.float32)
        for joint_num, i in enumerate(range(0, num_coordinates, step_size)):
            joint = self[joint_num]
            if min_score is not None and joint.score > -1:
                if joint.score < min_score:
                    for j in range(0, step_size-1):
                        numpy_array[j] = 0.0
                    if include_score:
                        numpy_array[-1] = -1
                    continue
            numpy_array[i] = joint.x
            numpy_array[i+1] = joint.y
            if is_3D:
                numpy_array[i+2] = joint.y
            if include_score:
                numpy_array[-1] = joint.score
        return numpy_array

    def to_dict(self) -> Dict[str, Any]:
        out_dict: Dict[str, Any] = {}
        for joint in self:
            out_dict[joint.name] = joint.to_dict()
        return out_dict

    def copy_from_dict(self, in_dict: Dict[str, Any]):
        joint_list: List[T] = []
        for joint_name, joint_dict in in_dict.items():
            joint_list.append(T.from_dict(joint_dict))
        self.copy_from_list(joint_list)
