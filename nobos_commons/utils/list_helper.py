from typing import List, Any


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
    for item_index in range(sequence_length, len(input_list), step=step_size):
        chunk_list.append(input_list[item_index - sequence_length])
    return chunk_list
