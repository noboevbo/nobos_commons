from typing import List, Dict

from nobos_commons.data_structures.base_iterable_property_class import BaseIterablePropertyClass
from nobos_commons.data_structures.skeletons.joint_2d import Joint2D


class SkeletonJointsBase(BaseIterablePropertyClass[Joint2D]):
    __dict__: Dict[str, Joint2D]

    def copy_from_list(self, joint_list: List[Joint2D]):
        """
        Takes joints from a lists and copies their parameters to the SkeletonJoints. It does not allow for duplicated
        joints in the list.
        :param joint_list: A list of Joint2Ds which parameters should be set in this skeleton_joints
        """
        added_joint_nums: List[int] = []
        for joint in joint_list:
            assert joint.num not in added_joint_nums, "Duplicated joint num {0} found!".format(joint.num)
            assert joint.num < len(self), "joint number {0} is not available in this skeleton.".format(joint.num)
            added_joint_nums.append(joint.num)
            self[joint.num].copy_from(joint)

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
