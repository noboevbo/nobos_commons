import numpy as np
import cv2

from nobos_commons.data_structures.bounding_box import BoundingBox
from nobos_commons.data_structures.constants.color_palette import DETECTION_COLOR_PALETTE
from nobos_commons.data_structures.constants.detection_classes import COCO_CLASSES


def draw_bb(image: np.ndarray, bb: BoundingBox):
    """
    Draws the given bounding box in the image
    :param image: The image in which the bounding box should be drawn
    :param bb: The bounding box too be drawn
    :return: The image with the visualized bounding box
    """
    color = DETECTION_COLOR_PALETTE[COCO_CLASSES.index(bb.label)]
    top_left_tuple = (bb.top_left.x, bb.top_left.y)
    bottom_right_tuple = (bb.bottom_right.x, bb.bottom_right.y)
    cv2.rectangle(image, top_left_tuple, bottom_right_tuple, color, 1)
    text_box_size = cv2.getTextSize(bb.label, cv2.FONT_HERSHEY_PLAIN, 1, 1)[0]
    text_box_bottom_right = bb.top_left.x + text_box_size[0] + 3, bb.top_left.y + text_box_size[1] + 4
    cv2.rectangle(image, top_left_tuple, text_box_bottom_right, color, -1)
    title = bb.label
    if bb.uid is not None:
        title = bb.uid
    cv2.putText(image, title, (bb.top_left.x, bb.top_left.y + text_box_size[1] + 4), cv2.FONT_HERSHEY_PLAIN, 1, [225, 255, 255], 1)
    return image
