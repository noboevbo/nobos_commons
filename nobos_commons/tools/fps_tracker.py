import time


class FPSTracker(object):
    def __init__(self, average_over_seconds: int = 0):
        self.average_over_seconds = average_over_seconds
        self.frame_counter = 0
        self.reference_start_time = None
        self.current_fps = -1

    def get_fps(self) -> float:
        current_time = time.time()
        self.frame_counter += 1

        if self.reference_start_time is None:
            self.reference_start_time = current_time

        if (current_time - self.reference_start_time) > self.average_over_seconds:
            self.current_fps = self.frame_counter / (current_time - self.reference_start_time)
            self.frame_counter = 0
            self.reference_start_time = current_time

        return self.current_fps

    def print_fps(self):
        fps = self.get_fps()
        print("FPS of the video is {:5.2f}".format(fps))
