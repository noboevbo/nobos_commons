from typing import List

from nobos_commons.data_structures.human import Limb2D
from nobos_commons.data_structures.simple_base_data_class import SimpleBaseDataClass


class SkeletonLimbsBase(SimpleBaseDataClass):
    def set_limbs_from_list(self, ordered_limb_list: List[Limb2D]):
        assert len(ordered_limb_list) == self.__len__()
        for limb_num in range(0, self.__len__()):
            limb = ordered_limb_list[limb_num]
            assert limb.num == limb_num, "Inconsistent limb number and index!"  # TODO: Without this it could be used more general...
            self[limb_num] = limb
