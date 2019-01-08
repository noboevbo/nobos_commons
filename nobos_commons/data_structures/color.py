from typing import Tuple

from nobos_commons.data_structures.singleton import Singleton


class Color(object):
    __slots__ = ["r", "g", "b"]

    def __init__(self, r: int, g: int, b: int):
        """
        Represents a RGB color.
        :param r: Red Channel
        :param g: Green Channel
        :param b: Blue Channel
        """
        assert self.is_color_channel_value(r) and self.is_color_channel_value(g) and self.is_color_channel_value(b)
        self.r = r
        self.g = g
        self.b = b

    @property
    def tuple_rgb(self) -> Tuple[int, int, int]:
        """
        Returns a RGB Tuple
        :return: RGB Tuple
        """
        return self.r, self.g, self.b

    @property
    def tuple_bgr(self) -> Tuple[int, int, int]:
        """
        Returns a BGR Tuple
        :return: BGR Tuple, e.g. for use in OpenCV functions
        """
        return self.b, self.g, self.r

    @property
    def hex(self) -> str:
        """
        Returns the hex value of the color
        :return: hex value of the color
        """
        return '#%02x%02x%02x' % (self.r, self.g, self.b)

    @classmethod
    def from_hex(cls, hex: str):
        """
        Calculates a RGB value from hex value and returns a RGB Color.
        :param hex: The hex color string
        :return: RGB Color
        """
        rgb_tuple = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
        return Color(r=rgb_tuple[0], g=rgb_tuple[1], b=rgb_tuple[2])

    @classmethod
    def is_color_channel_value(cls, value: int):
        """
        Checks if a given integer value is a valid color channel value
        :param value: The value which should be used as a color channel value
        :return: True if it is a valid color channel value, else false
        """
        return 0 <= value <= 255


class Colors(Singleton):
    """
    Contains various predefined colors.
    """
    grey = Color(128, 128, 128)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    blue = Color(0, 0, 255)
    black = Color(0, 0, 0)
    white = Color(255, 255, 255)


