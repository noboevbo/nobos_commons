from typing import Generic

from nobos_commons.data_structures.generic import NUM


class ImageSize(object):
    __slots__ = ['width', 'height']

    def __init__(self, width: int, height: int):
        """
        Represents the size of a image
        :param width: The width of the image
        :param height: The height of the image
        """
        self.width = width
        self.height = height

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, ImageSize):
            return self.width == other.width and \
                   self.height == other.height
        return False


class Coord2D(Generic[NUM]):
    __slots__ = ['x', 'y']

    def __init__(self, x: NUM, y: NUM):
        """
        Represents coordinates in a two dimensional coordinate system.
        :param x: The x coordinate
        :param y: The y coordinate
        """
        self.x = x
        self.y = y


class Coord3D(Coord2D, Generic[NUM]):
    __slots__ = ['x', 'y', 'z']

    def __init__(self, x: NUM, y: NUM, z: NUM):
        """
        Represents coordinates in a three dimensional coordinate system.
        :param x: The x coordinate
        :param y: The y coordinate
        :param z: The z coordinate
        """
        super().__init__(x, y)
        self.z = z


class Space3DSize(Coord3D):
    def __init__(self, x: int, y: int, z: int):
        """
        Represents a three dimensional spaces size.
        :param x: The size of the first dimension
        :param y: The size of the second dimension
        :param z: The size of the third dimension
        """
        super().__init__(x, y, z)


class Vec2D(Coord2D, Generic[NUM]):
    def __init__(self, x: NUM, y: NUM):
        """
        Represents a two dimensional vector
        :param x: x coordinate of the vector
        :param y: y coordinate of the vector
        """
        super().__init__(x, y)


class Vec3D(Coord3D, Generic[NUM]):
    def __init__(self, x: NUM, y: NUM, z: NUM):
        """
        Represents a two dimensional vector
        :param x: x coordinate of the vector
        :param y: y coordinate of the vector
        :param z: z coordinate of the vector
        """
        super().__init__(x, y, z)
