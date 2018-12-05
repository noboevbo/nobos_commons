from typing import TypeVar, Generic, Type

from nobos_commons.data_structures.skeletons.skeleton_base import SkeletonBase


class SkeletonConverter(object):

    def get_converted_skeleton(self, skeleton_a: SkeletonBase) -> SkeletonBase:
        raise NotImplementedError
