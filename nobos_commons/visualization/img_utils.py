from typing import List

import cv2


def add_img_title(img, title, font_scale: int =1):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, title, (0, 30), font, font_scale, (0, 0, 255), 1, cv2.LINE_AA)


def rgb_to_bgr_color(rgb_color: List[int]):
    return [rgb_color[2], rgb_color[1], rgb_color[0]]