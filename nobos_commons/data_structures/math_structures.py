import numpy as np

class Quaternion(object):
    __slots__ = ['_quaternion']

    def __init__(self, w: float, x: float, y: float, z: float):
        """
        Represents a triangle with radian angles.
        :param w: The real component
        :param x: The first imaginary component
        :param y: The second imaginary component
        :param z: The third imaginary component
        """
        self._quaternion = np.array([w, x, y, z], dtype=np.double)

    def to_numpy_array(self):
        """
        Returns the quaternion as numpy array (as internally stored)
        :return: np.array([w, x, y, z], dtype=np.double)
        """
        return self._quaternion

    def list(self):
        """
        Convernts and returns the quaternion as list
        :return: list [w, x, y, z]
        """
        return self._quaternion.tolist()

    @property
    def w(self):
        return self._quaternion[0]

    @property
    def x(self):
        return self._quaternion[1]

    @property
    def y(self):
        return self._quaternion[2]

    @property
    def z(self):
        return self._quaternion[3]

