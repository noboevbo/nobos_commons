import os
import time

import cv2
import numpy as np
from nobos_commons.utils.file_helper import get_img_paths_from_folder


class ImgDirProvider(object):
    def __init__(self,
                 img_dir: str,
                 fps: int = None):
        self.img_dir = img_dir
        assert os.path.exists(img_dir), 'Image directory not found!'
        self.img_paths = sorted(get_img_paths_from_folder(img_dir))
        self.fps = fps

    def get_frame(self) -> np.ndarray:
        assert len(self.img_paths) > 0, 'No images found'

        for img_path in self.img_paths:
            if self.fps is not None:
                start = time.time()
            img = cv2.imread(img_path)
            yield img

            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                return None

            if self.fps is not None:
                time.sleep(max(1. / self.fps - (time.time() - start), 0))

# if __name__ == '__main__':
#     provider = ImgDirProvider("/home/dennis/Downloads/tmp/out", fps = 120)
#     fps_logger = FPSLogger(average_over_seconds=2)
#     for i in provider.get_frame():
#         cv2.imshow('img_dir', i)
#         fps_logger.print_fps()

