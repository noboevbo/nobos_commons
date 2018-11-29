from typing import List

from nobos_commons.data_structures.simple_base_data_class import SimpleBaseDataClass
from nobos_commons.data_structures.skeletons.limb_2d import Limb2D


class SkeletonLimbsBase(SimpleBaseDataClass[Limb2D]):
    def set_limbs_from_list(self, ordered_limb_list: List[Limb2D]):
        assert len(ordered_limb_list) == self.__len__()
        for limb_num in range(0, self.__len__()):
            limb = ordered_limb_list[limb_num]
            assert limb.num == limb_num, "Inconsistent limb number and index!"  # TODO: Without this it could be used more general...
            self[limb_num].copy_from(limb)

    def num_limbs_set(self):
        count = 0
        for limb in self:
            if limb.is_set:
                count += 1
        return count
