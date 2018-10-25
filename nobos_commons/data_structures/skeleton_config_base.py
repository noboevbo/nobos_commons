from collections import OrderedDict
from typing import List

from nobos_commons.data_structures.color import Color


class SkeletonConfigBase:
    @property
    def joints(self) -> OrderedDict:
        raise NotImplementedError

    @property
    def limbs(self) -> List[List[int]]:
        raise NotImplementedError

    @property
    def left_parts(self) -> List[str]:
        raise NotImplementedError

    @property
    def right_parts(self) -> List[str]:
        raise NotImplementedError

    @property
    def limb_colors(self) -> List[Color]:
        raise NotImplementedError

    @property
    def joint_colors(self) -> List[Color]:
        raise NotImplementedError

    def get_joint_name_by_id(self, joint_id):
        return list(self.joints.items())[joint_id][0]