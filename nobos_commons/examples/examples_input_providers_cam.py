import cv2

from nobos_commons.data_structures.dimension import ImageSize
from nobos_commons.input_providers.camera.img_dir_provider import ImgDirProvider
from nobos_commons.input_providers.camera.webcam_provider import WebcamProvider, WebcamProviderAsync
from nobos_commons.tools.fps_tracker import FPSTracker


def webcam_example():
    provider = WebcamProvider(fps=60, image_size=ImageSize(1280, 720), camera_number=0)
    fps_tracker = FPSTracker()
    for i in provider.get_data():
        cv2.imshow('webcam', i)
        fps_tracker.print_fps()

def webcam_example_async():
    provider = WebcamProviderAsync(fps=60, image_size=ImageSize(1280, 720), camera_number=0)
    fps_tracker = FPSTracker()
    for i in provider.get_data():
        cv2.imshow('webcam', i)
        fps_tracker.print_fps()

def img_dir_example(img_dir: str):
    provider = ImgDirProvider(img_dir, fps=120)
    fps_tracker = FPSTracker(average_over_seconds=2)
    for i in provider.get_data():
        cv2.imshow('img_dir', i)
        fps_tracker.print_fps()


if __name__ == "__main__":
    # webcam_example_async()
    webcam_example()
    # img_dir_example("/media/disks/beta/datasets/ofp_tests/ofp_parkplatz_walking_02/FrontCamera")
