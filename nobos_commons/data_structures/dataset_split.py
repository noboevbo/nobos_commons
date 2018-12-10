from nobos_commons.data_structures.constants.dataset_slit_type import DatasetSplitType


class DatasetSplit(object):
    __slots__ = ['dataset_name', 'dataset_split_type']

    def __init__(self, dataset_name: str, dataset_split_type: DatasetSplitType):
        self.dataset_name = dataset_name
        self.dataset_split_type = dataset_split_type
