from typing import List, Dict

from nobos_commons.data_structures.human import Joint2D
from nobos_commons.data_structures.simple_base_data_class import SimpleBaseDataClass


class SkeletonJointsBase(SimpleBaseDataClass):
    __dict__: Dict[str, Joint2D]
    def set_joints_from_list(self, ordered_joint_list: List[Joint2D]):
        assert len(ordered_joint_list) == self.__len__()
        for joint_num in range(0, self.__len__()):
            joint = ordered_joint_list[joint_num]
            assert joint.num == joint_num, "Inconsistent joint number and index!"  # TODO: Without this it could be used more general...
            self[joint_num] = joint