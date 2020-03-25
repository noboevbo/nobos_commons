from typing import Union

import numpy as np

from nobos_commons.data_structures.dimension import Vec3D


# https://stackoverflow.com/questions/4870393/rotating-coordinate-system-via-a-quaternion
def _multiply_quaternion(q1: 'Quaternion', q2: 'Quaternion'):
    w1, x1, y1, z1 = q1._quaternion
    w2, x2, y2, z2 = q2._quaternion
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return Quaternion(w, x, y, z)

# def euler_to_quaternion(roll, pitch, yaw):
#     qx = np.sin(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) - np.cos(roll / 2) * np.sin(pitch / 2) * np.sin(yaw / 2)
#     qy = np.cos(roll / 2) * np.sin(pitch / 2) * np.cos(yaw / 2) + np.sin(roll / 2) * np.cos(pitch / 2) * np.sin(yaw / 2)
#     qz = np.cos(roll / 2) * np.cos(pitch / 2) * np.sin(yaw / 2) - np.sin(roll / 2) * np.sin(pitch / 2) * np.cos(yaw / 2)
#     qw = np.cos(roll / 2) * np.cos(pitch / 2) * np.cos(yaw / 2) + np.sin(roll / 2) * np.sin(pitch / 2) * np.sin(yaw / 2)
#
#     return [qw, qx, qy, qz]

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

    def conjugate(self):
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def __mul__(self, other: Union['Quaternion', Vec3D]):
        if isinstance(other, Quaternion):
            return _multiply_quaternion(self, other)
        elif isinstance(other, Vec3D):
            lx = self.x * 2
            ly = self.y * 2
            lz = self.z * 2
            xx = self.x * lx
            yy = self.y * ly
            zz = self.z * lz
            xy = self.x * ly
            xz = self.x * lz
            yz = self.y * lz
            wx = self.w * lx
            wy = self.w * ly
            wz = self.w * lz

            u = (1 - (yy + zz)) * other.x + (xy - wz) * other.y + (xz + wy) * other.z
            v = (xy + wz) * other.x + (1 - (xx + zz)) * other.y + (yz - wx) * other.z
            w = (xz - wy) * other.x + (yz + wx) * other.y + (1 - (xx + yy)) * other.z
            # vec_quaternion = Quaternion(0.0, other.x, other.y, other.z)
            return [u, v, w]


if __name__ == "__main__":
    q1 = Quaternion(0, 1, 0, 0)
    q2 = Vec3D(0, 0, 1)

    test = q1 * q2
    a = 1

