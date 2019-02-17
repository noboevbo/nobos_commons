# from typing import Any, Dict
#
# from nobos_commons.data_structures.constants.dataset_split import DatasetSplitType
#
#
# class DatasetSplit(object):
#     __slots__ = ['dataset_name', 'split_type']
#
#     def __init__(self, dataset_name: str, split_type: DatasetSplitType):
#         self.dataset_name = dataset_name
#         self.split_type = split_type
#
#     def to_dict(self) -> Dict[str, Any]:
#         return {
#             'dataset_name': self.dataset_name,
#             'split_type': self.split_type.name
#         }
#
#     @staticmethod
#     def from_dict(dict_in: Dict[str, Any]) -> 'DatasetSplit':
#         return DatasetSplit(dataset_name=dict_in['dataset_name'],
#                             split_type=DatasetSplitType[dict_in['split_type']])
