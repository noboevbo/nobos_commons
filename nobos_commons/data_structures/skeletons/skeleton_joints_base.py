from typing import List, Dict

from nobos_commons.data_structures.simple_base_data_class import SimpleBaseDataClass
from nobos_commons.data_structures.skeletons.joint_2d import Joint2D


class SkeletonJointsBase(SimpleBaseDataClass[Joint2D]):
    __dict__: Dict[str, Joint2D]

    def copy_from_list(self, joint_list: List[Joint2D]):
        added_joint_nums: List[int] = []
        for joint in joint_list:
            assert joint.num not in added_joint_nums, "Duplicated joint num {0} found!".format(joint.num)
            added_joint_nums.append(joint.num)
            self[joint.num].copy_from(joint)

    # def set_joints_from_list(self, ordered_joint_list: List[Joint2D]):
    #     assert len(ordered_joint_list) == self.__len__()
    #     for joint_num in range(0, self.__len__()):
    #         joint = ordered_joint_list[joint_num]
    #         assert joint.num == joint_num, "Inconsistent joint number and index!"  # TODO: Without this it could be used more general...
    #         self[joint_num].copy_from(joint)
    #
    # def set_joints_from_dict(self, joint_dict: Dict[int, Joint2D]):


    def num_joints_set(self):
        count = 0
        for joint in self:
            if joint.is_set:
                count += 1
        return count
