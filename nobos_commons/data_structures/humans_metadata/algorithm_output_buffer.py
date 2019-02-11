from collections import deque
from typing import List, Dict

from nobos_commons.data_structures.humans_metadata.algorithm_output_buffer_entry import AlgorithmOutputBufferEntry


class AlgorithmOutputBuffer(object):
    def __init__(self, buffer_size: int = 10):
        self.buffer_size = buffer_size
        self.__store = {}
        self.__last_frame_updated: Dict[str, int] = {}

    def add(self, outputs: List[AlgorithmOutputBufferEntry], frame_nr: int):
        # Remove the existing cache if more than one frame passed
        ids_to_delete = []
        for identifier, last_frame_updated in self.__last_frame_updated.items():
            if last_frame_updated < frame_nr-1:
                ids_to_delete.append(identifier)
        for identifier in ids_to_delete:
            del self.__store[identifier]
            del self.__last_frame_updated[identifier]

        for output in outputs:
            if output.identifier not in self.__store:
                self.__store[output.identifier] = deque(maxlen=self.buffer_size)
                self.__last_frame_updated[output.identifier] = frame_nr

            self.__store[output.identifier].append(output.algorithm_output)
            self.__last_frame_updated[output.identifier] = frame_nr

    def get_all(self, only_full_buffer: bool = False):
        if not only_full_buffer:
            return self.__store
        output = {}
        for identifier, buffer in self.__store.items():
            if len(buffer) == self.buffer_size:
                output[identifier] = buffer
        return output

    def get(self, identifier: str):
        return self.__store[identifier]
