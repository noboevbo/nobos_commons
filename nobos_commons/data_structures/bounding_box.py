from nobos_commons.data_structures.dimension import Coord2D


class BoundingBox(object):
    __slots__ = ["top_left", "top_right", "bottom_left", "bottom_right", "width", "height", "label", "class_index", "uid"]

    def __init__(self, top_left: Coord2D, bottom_right: Coord2D, label: str = "None", uid: str = None):
        """
        Bounding box class which represents a bounding box and various derived values like the corner coordinates,
        width and height.
        :param top_left: The top left coordinate of the bounding box
        :param bottom_right: The bottom right coordinate of the bounding box
        :param label: The label of the bounding box (usually the class)
        :param uid: A unique id of the bounding box (e.g. for object tracking)
        """
        self.top_left = top_left
        self.top_right = Coord2D(x=bottom_right.x, y=top_left.y)
        self.bottom_left = Coord2D(x=top_left.x, y=bottom_right.y)
        self.bottom_right = bottom_right
        self.width = bottom_right.x - top_left.x
        self.height = bottom_right.y - top_left.y
        self.label = label
        self.uid = uid
