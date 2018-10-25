from typing import Tuple


class Color(object):
    __slots__ = ["r", "g", "b"]

    def __init__(self, r: int, g: int, b: int):
        assert self.is_color_value(r) and self.is_color_value(g) and self.is_color_value(b)
        self.r = r
        self.g = g
        self.b = b

    @property
    def tuple_rgb(self) -> Tuple[int, int, int]:
        return self.r, self.g, self.b

    @property
    def tuple_bgr(self) -> Tuple[int, int, int]:
        return self.b, self.g, self.r

    @classmethod
    def from_hex(cls, hex: str):
        rgb_tuple = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
        return Color(r=rgb_tuple[0], g=rgb_tuple[1], b=rgb_tuple[2])

    @staticmethod
    def is_color_value(value: int):
        return 0 <= value <= 255
