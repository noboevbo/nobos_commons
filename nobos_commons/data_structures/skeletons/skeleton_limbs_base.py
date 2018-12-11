from typing import List, Dict, Any

from nobos_commons.data_structures.base_iterable_property_class import BaseIterablePropertyClass
from nobos_commons.data_structures.skeletons.limb_2d import Limb2D


class SkeletonLimbsBase(BaseIterablePropertyClass[Limb2D]):
    @property
    def names(self) -> List[str]:
        names = []
        for key in self.__dict__.keys():
            names.append(key[1:])
        return names

    def copy_from_list(self, limb_list: List[Limb2D]):
        """
        Takes limbs from a lists and copies their parameters to the SkeletonLimbs. It does not allow for duplicated
        limbs in the list.
        :param limb_list: A list of Limb2Ds which parameters should be set in this skeleton_limbs
        """
        added_limb_nums: List[int] = []
        for limb in limb_list:
            assert limb.num not in added_limb_nums, "Duplicated limb num {0} found!".format(limb.num)
            assert limb.num < len(self), "limb number {0} is not available in this skeleton.".format(limb.num)
            added_limb_nums.append(limb.num)
            self[limb.num].copy_from(limb)

    def copy_from_other(self, other: 'SkeletonLimbsBase'):
        """
        Copies the values from the other SkeletonLimbs
        :param other: other skeleton limbs, must be of the same type
        """
        assert type(self) == type(other), 'Can\'t copy values from another type!'
        for limb in other:
            self[limb.num].copy_from(limb)

    def num_limbs_set(self):
        """
        Returns the number of limbs which are actually parameterized.
        :return: The number of limbs which are actually parameterized.
        """
        count = 0
        for limb in self:
            if limb.is_set:
                count += 1
        return count

    def to_dict(self) -> Dict[str, Any]:
        out_dict: Dict[str, Any] = {}
        for limb in self:
            out_dict[str(limb.name)] = limb.to_dict()
        return out_dict

    def copy_from_dict(self, in_dict: Dict[str, Any]):
        limb_list: List[Limb2D] = []
        for limb_name, limb_dict in in_dict.items():
            limb_list.append(Limb2D.from_dict(limb_dict))
        self.copy_from_list(limb_list)
