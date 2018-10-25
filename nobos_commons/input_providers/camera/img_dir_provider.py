import os
import time

import cv2
import numpy as np

from nobos_commons.input_providers.input_provider_base import InputProviderBase
from nobos_commons.utils.file_helper import get_img_paths_from_folder


class ImgDirProvider(InputProviderBase):
    def __init__(self,
                 img_dir: str,
                 fps: int = None):
        """
        Provides images from a given image directory.
        :param img_dir: The directory which contains the images
        :param fps: Forced fps for the image delivery. May be limited by disk io...
        """
        self.img_dir = img_dir
        assert os.path.exists(img_dir), 'Image directory not found!'
        self.img_paths = sorted(get_img_paths_from_folder(img_dir))
        self.fps = fps

    def get_data(self) -> np.ndarray:
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
