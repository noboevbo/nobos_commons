from typing import Any, Dict

from nobos_commons.data_structures.constants.dataset_slit_type import DatasetSplitType


class DatasetSplit(object):
    __slots__ = ['dataset_name', 'dataset_split_type']

    def __init__(self, dataset_name: str, dataset_split_type: DatasetSplitType):
        self.dataset_name = dataset_name
        self.dataset_split_type = dataset_split_type

    def to_dict(self) -> Dict[str, Any]:
        return {
            'dataset_name': self.dataset_name,
            'dataset_split_type': self.dataset_split_type.name
        }

    @staticmethod
    def from_dict(dict_in: Dict[str, Any]) -> 'DatasetSplit':
        return DatasetSplit(dataset_name=dict_in['dataset_name'],
                            dataset_split_type=dict_in['dataset_split_type'])
