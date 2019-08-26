from typing import Dict, Any

from nobos_commons.data_structures.dimension import Coord3D


class BoundingBox3D(object):
    __slots__ = ["top_left", "top_right", "bottom_left", "bottom_right", "width", "height", "depth", "label"]

    def __init__(self, top_left: Coord3D, bottom_right: Coord3D, label: str = "None"):
        """
        Bounding box class which represents a bounding box and various derived values like the corner coordinates,
        width and height.
        :param top_left: The top left coordinate of the bounding box
        :param bottom_right: The bottom right coordinate of the bounding box
        :param label: The label of the bounding box (usually the class)
        """
        self.top_left = top_left
        self.top_right = Coord3D(x=bottom_right.x, y=top_left.y, z=bottom_right.z)
        self.bottom_left = Coord3D(x=top_left.x, y=bottom_right.y, z=top_left.z)
        self.bottom_right = bottom_right
        self.width = bottom_right.x - top_left.x
        self.height = bottom_right.y - top_left.y
        self.depth = abs(bottom_right.z - top_left.z)
        self.label = label

    def to_dict(self) -> Dict[str, Any]:
        return {
            "label": self.label,
            "width": self.width,
            "height": self.height,
            "depth": self.depth,
            "top_left": [self.top_left.x, self.top_left.y, self.top_left.z],
            "top_right": [self.top_right.x, self.top_right.y, self.top_right.z],
            "bottom_left": [self.bottom_left.x, self.bottom_left.y, self.bottom_left.z],
            "bottom_right": [self.bottom_right.x, self.bottom_right.y, self.bottom_right.z]
        }
