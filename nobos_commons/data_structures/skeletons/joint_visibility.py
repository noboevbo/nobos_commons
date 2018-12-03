from enum import Enum


class JointVisibility(Enum):
    VISIBLE = 1  # The joint is clearly visible
    INVISIBLE = 2  # The joint is invisible, e.g. occluded
    ABSENT = 3  # The joint is not in the camera field
