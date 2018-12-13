from collections import deque
from typing import List, Dict

from nobos_commons.data_structures.human import Human
from nobos_commons.data_structures.image_content import ImageContent
from nobos_commons.data_structures.image_content_buffer_entry import HumanContentBufferEntry


class ImageContentBuffer(object):
    buffer_count: int = 0
    __image_contents: List[ImageContent] = None
    __human_content_buffers: Dict[str, HumanContentBufferEntry]

    def __init__(self, buffer_size: int = 10):
        self.buffer_size = buffer_size
        self.buffer_count = 0
        self.__image_contents = deque(maxlen=buffer_size)
        self.__human_content_buffers = {}

    def add(self, image_content: ImageContent):
        self.buffer_count += 1
        self.__image_contents.append(image_content)
        updated_keys = []
        if image_content.humans is not None:
            for human in image_content.humans:
                if human.uid in self.__human_content_buffers.keys():
                    self.__human_content_buffers[human.uid].update(human, self.buffer_count)
                    updated_keys.append(human.uid)
                else:
                    self.__human_content_buffers[human.uid] = HumanContentBufferEntry(human_id=human.uid, human=human,
                                                                                      buffer_count=self.buffer_count,
                                                                                      buffer_size=self.buffer_size)

        for key, buffer in self.__human_content_buffers.items():
            if key in updated_keys:
                continue
            buffer.update(None, self.buffer_count)
        self.__clean_human_content_buffers()

    def __clean_human_content_buffers(self):
        keys_to_delete = []
        for key, buffer in self.__human_content_buffers.items():
            if buffer.last_added < self.buffer_count - self.buffer_size:
                keys_to_delete.append(key)
        for key in keys_to_delete:
            del self.__human_content_buffers[key]

    def get_human_data_buffer_by_id(self, human_id: str) -> List[Human]:
        return self.__human_content_buffers[human_id].human_content_buffer

    def get_human_content_buffers(self) -> Dict[str, List[Human]]:
        result: Dict[str, List[Human]] = {}
        for key, human_content_buffer in self.__human_content_buffers.items():
            result[key] = human_content_buffer.human_content_buffer
        return result

    def get_last(self):
        if len(self.__image_contents) == 0:
            return None
        return self.__image_contents[-1]

    def get_last_human_content(self):
        if len(self.__image_contents) == 0:
            return None
        return self.__image_contents[-1].humans
