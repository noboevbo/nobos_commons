from itertools import zip_longest
from typing import List, Any

import numpy as np

from nobos_commons.utils.numpy_helper import set_or_vstack


def get_chunks_by_list_sampler(input_list: List[Any], sequence_length: int, step_size: int = 1) -> List[List[Any]]:
    """
    Samples a list in a number of chunks of length sequence_length. Creates chunks by sampling the input_list, e.g.
     [0 to sequence_length, step_size to sequence_length + step_size; ...]
    :param input_list: Ordered list of objects which should be split into chunks
    :param sequence_length: The length of one chunk
    :param step_size: The step_size in which the input_list should be sampled
    :return: numpy_array with shape [time_frame_length, 1, self.feature_vec_length]
    """
    chunk_list: List[List[Any]] = []
    for item_index in range(sequence_length, len(input_list), step_size):
        chunk_list.append(input_list[item_index - sequence_length])
    return chunk_list


def split_list(input_list: List[Any], split_size: int, fill_value: Any = None):
    args = [iter(input_list)] * split_size
    return zip_longest(fillvalue=fill_value, *args)


def split_list_stepwise(input_list: List[Any], split_size: int, step_size: int, fill_value: Any = None,
                        every_n_element: int = 1) -> List[List[Any]]:
    assert fill_value is not None or len(input_list) >= split_size, \
        "Input list of length '{}' is less than split size '{}' and no fill_value is given".format(len(input_list),
                                                                                                   split_size)
    # TODO: Create a handler which checks for splits which contain only zeros or so and removes them
    output_splits: List[List[Any]] = []
    if len(input_list) < split_size * every_n_element:
        for i in range(0, split_size - len(input_list)):
            input_list.append(fill_value)

    for input_list_index in range(0, len(input_list) - ((split_size*every_n_element) - 1), step_size): # TODO: is this -1 correct?
        output_split: List[Any] = []
        for output_split_index, input_list_index_for_output_split in \
                enumerate(range(input_list_index, input_list_index + (split_size*every_n_element), every_n_element)):
            output_split.append(input_list[input_list_index_for_output_split])
        output_splits.append(output_split)
    return output_splits




