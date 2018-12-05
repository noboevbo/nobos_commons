from typing import Type, Dict, Tuple, Any

from nobos_commons.data_structures.singleton import Singleton
from nobos_commons.data_structures.skeletons.skeleton_base import SkeletonBase
from nobos_commons.data_structures.skeletons.skeleton_coco import SkeletonCoco
from nobos_commons.data_structures.skeletons.skeleton_jhmdb import SkeletonJhmdb
from nobos_commons.data_structures.skeletons.skeleton_stickman import SkeletonStickman
from nobos_commons.tools.skeleton_converters.skeleton_converter_base import SkeletonConverter
from nobos_commons.tools.skeleton_converters.skeleton_converter_coco_to_stickman import SkeletonConverterCocoToStickman
from nobos_commons.tools.skeleton_converters.skeleton_converter_jhmdb_to_stickman import \
    SkeletonConverterJhmdbToStickman


class SkeletonConverterDefinition(object):
    __slots__ = ['skeleton_type_a', 'skeleton_type_b', 'skeleton_converter']

    def __init__(self, skeleton_type_a: Type[SkeletonBase], skeleton_type_b: Type[SkeletonBase], skeleton_converter):
        self.skeleton_type_a = skeleton_type_a
        self.skeleton_type_b = skeleton_type_b
        self.skeleton_converter = skeleton_converter


class SkeletonConverterFactory(metaclass=Singleton):
    def __init__(self):
        self.__skeleton_converter_definition: Dict[Tuple[Type[SkeletonBase], Type[SkeletonBase]], Any] = {
            (SkeletonCoco, SkeletonStickman): SkeletonConverterCocoToStickman(),
            (SkeletonJhmdb, SkeletonStickman): SkeletonConverterJhmdbToStickman()
        }

    def get_skeleton_converter(self, skeleton_type_a: Type[SkeletonBase], skeleton_type_b: Type[SkeletonBase]) -> SkeletonConverter:
        assert (skeleton_type_a, skeleton_type_b) in self.__skeleton_converter_definition, \
            'No converter found for types {0} and {1}'.format(skeleton_type_a, skeleton_type_b)
        return self.__skeleton_converter_definition[(skeleton_type_a, skeleton_type_b)]
