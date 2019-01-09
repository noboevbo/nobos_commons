import cv2
import numpy as np

from nobos_commons.data_structures.dimension import ImageSize
from nobos_commons.input_providers.input_provider_base import InputProviderBase


class WebcamProvider(InputProviderBase):
    def __init__(self,
                 camera_number: int = 0,
                 image_size: ImageSize = ImageSize(width=1280, height=720),
                 fps: int = 60):
        """
        Provides frames captured from a webcam. Uses OpenCV internally.
        :param camera_number: The cameras id
        :param image_size: The image size which should be used, may be limited by camera parameters
        :param fps: The fps on which the frames should be grabbed, may be limited by camera parameters
        """
        self.cap = cv2.VideoCapture(camera_number)

        self.image_size = image_size
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.image_size.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.image_size.height)
        self.cap.set(cv2.CAP_PROP_FPS, fps)

    def get_data(self) -> np.ndarray:
        assert self.cap.isOpened(), 'Cannot capture source'

        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                yield frame

                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    return None

            else:
                return None

        self.cap.release()

    def stop(self):
        self.cap.release()

