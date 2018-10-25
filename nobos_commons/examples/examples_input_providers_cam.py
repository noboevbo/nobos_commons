import cv2

from nobos_commons.input_providers.camera.img_dir_provider import ImgDirProvider
from nobos_commons.input_providers.camera.webcam_provider import WebcamProvider
from nobos_commons.tools.fps_tracker import FPSTracker


def webcam_example():
    provider = WebcamProvider()
    fps_tracker = FPSTracker()
    for i in provider.get_frame():
        cv2.imshow('webcam', i)
        fps_tracker.print_fps()


def img_dir_example():
    provider = ImgDirProvider("/home/dennis/Downloads/tmp/out", fps=120)
    fps_tracker = FPSTracker(average_over_seconds=2)
    for i in provider.get_frame():
        cv2.imshow('img_dir', i)
        fps_tracker.print_fps()