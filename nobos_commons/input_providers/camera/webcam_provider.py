import cv2
import numpy as np

from nobos_commons.data_structures.dimension import ImageSize


class WebcamProvider(object):
    def __init__(self,
                 camera_number: int = 0,
                 image_size: ImageSize = ImageSize(width=1280, height=720),
                 fps: int = 60):
        self.cap = cv2.VideoCapture(camera_number)

        self.image_size = image_size
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.image_size.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.image_size.height)
        self.cap.set(cv2.CAP_PROP_FPS, fps)

    def get_frame(self) -> np.ndarray:
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


# if __name__ == '__main__':
#     provider = WebcamProvider()
#     fps_logger = FPSLogger()
#     for i in provider.get_frame():
#         cv2.imshow('webcam', i)
#         fps_logger.print_fps()

