from typing import Dict, Any

from nobos_commons.data_structures.skeletons.joint_3d import Joint3D
from nobos_commons.data_structures.skeletons.limb_2d import Limb2D


class Limb3D(Limb2D):
    __slots__ = ['_num', '_joint_from', '_joint_to', 'score']

    def __init__(self, num: int, joint_from: Joint3D, joint_to: Joint3D, score: float = -1):
        """
        :param num: The number of the limb in the skeleton configuration
        :param joint_from: The joint from which the limb goes
        :param joint_to: The joint to which the limb goes
        :param score: The score of the limb
        """
        super().__init__(num, joint_from, joint_to, score)
        self._joint_from: Joint3D = joint_from
        self._joint_to: Joint3D = joint_to

    @property
    def joint_from(self) -> Joint3D:
        return self._joint_from

    @property
    def joint_to(self) -> Joint3D:
        return self._joint_to

    # Serialization

    @staticmethod
    def from_dict(joint_3d_dict: Dict[str, Any]) -> 'Limb3D':
        return Limb3D(num=joint_3d_dict['num'],
                      joint_from=Joint3D.from_dict(joint_3d_dict['joint_from']),
                      joint_to=Joint3D.from_dict(joint_3d_dict['joint_to']),
                      score=float(joint_3d_dict['score']))
