import random
import sys

from nobos_commons.data_structures.bounding_box import BoundingBox
from nobos_commons.data_structures.dimension import Coord2D, ImageSize
from nobos_commons.data_structures.human import HumanPoseResult
from nobos_commons.data_structures.skeletons.skeleton_joints_base import SkeletonJointsBase


def get_human_bounding_box_from_joints(joints: SkeletonJointsBase, image_size: ImageSize):
    min_x = sys.maxsize
    min_y = sys.maxsize
    max_x = 0
    max_y = 0
    for joint in joints:
        x = joint.x
        y = joint.y
        min_x = min_x if x > min_x else x
        min_y = min_y if y > min_y else y
        max_x = max_x if x < max_x else x
        max_y = max_y if y < max_y else y

    bb_width = max_x - min_x
    bb_height = max_y - min_y

    bb_expand_width = 0.15 * bb_width
    bb_expand_height = 0.15 * bb_height

    min_x = min_x - bb_expand_width
    min_y = min_y - bb_expand_height
    max_x = max_x + bb_expand_width
    max_y = max_y + bb_expand_height

    min_x = min_x if min_x > 0 else 0
    min_y = min_y if min_y > 0 else 0
    max_x = max_x if max_x < image_size.width else image_size.width
    max_y = max_y if max_y < image_size.height else image_size.height

    return BoundingBox(top_left=Coord2D(x=int(min_x), y=int(min_y)),
                       bottom_right=Coord2D(x=int(max_x), y=int(max_y)), label="person")


def get_random_bounding_box(width, height, bb_min_size=(5, 5)):
    x = random.randrange(0, width - bb_min_size[0])
    y = random.randrange(0, height - bb_min_size[1])
    x_max = random.randrange(x + bb_min_size[0], width)
    y_max = random.randrange(y + bb_min_size[1], height)
    return BoundingBox(top_left=Coord2D(x=x, y=y), bottom_right=Coord2D(x=x_max, y=y_max))
