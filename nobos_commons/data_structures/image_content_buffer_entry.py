from collections import deque
from typing import List

from nobos_commons.data_structures.human import Human


class HumansBufferEntry(object):
    human_id: str
    last_added: int
    human_content_buffer: List[Human]

    def __init__(self, human_id: str, buffer_count: int, human: Human, buffer_size: int):
        self.human_id = human_id
        self.last_added = buffer_count
        self.human_content_buffer = deque(maxlen=buffer_size)
        self.human_content_buffer.append(human)

    def update(self, human: Human, buffer_count: int):
        if human is not None:
            self.last_added = buffer_count
        self.human_content_buffer.append(human)
