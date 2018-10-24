from typing import Generic

from nobos_commons.data_structures.generic import NUM


class ImageSize(object):
    __slots__ = ['width', 'height']

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height


class Coord2D(Generic[NUM]):
    __slots__ = ['x', 'y']

    def __init__(self, x: NUM, y: NUM):
        self.x = x
        self.y = y


class Coord3D(Coord2D, Generic[NUM]):
    __slots__ = ['x', 'y', 'z']
    z: NUM

    def __init__(self, x: NUM, y: NUM, z: NUM):
        super().__init__(x, y)
        self.z = z


class Dim3D(Coord3D):

    def __init__(self, x: int, y: int, z: int):
        super().__init__(x, y, z)


class Vec2D(Coord2D, Generic[NUM]):
    def __init__(self, x: NUM, y: NUM):
        super().__init__(x, y)


class Vec3D(Coord3D, Generic[NUM]):
    def __init__(self, x: NUM, y: NUM, z: NUM):
        super().__init__(x, y, z)