from collections import OrderedDict
from typing import List


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
    def limb_colors(self) -> List[List[int]]:
        raise NotImplementedError

    @property
    def joint_colors(self) -> List[List[int]]:
        raise NotImplementedError

    # TODO: Colors -> Datastructure instead list ..

    def get_joint_name_by_id(self, joint_id):
        return list(self.joints.items())[joint_id][0]