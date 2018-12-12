from typing import Dict, Any

from nobos_commons.data_structures.skeletons.joint_2d import Joint2D


class Limb2D(object):
    def __init__(self, num: int, joint_from: Joint2D, joint_to: Joint2D, score: float = -1):
        __slots__ = ['_num', '_joint_from', '_joint_to', 'score']
        """
        :param num: The number of the limb in the skeleton configuration
        :param joint_from: The joint from which the limb goes
        :param joint_to: The joint to which the limb goes
        :param score: The score of the limb
        """
        self._num: int = num
        self._joint_from: Joint2D = joint_from
        self._joint_to: Joint2D = joint_to
        self._score: float = score

    @property
    def matched_score(self) -> float:
        return self.score + self.joint_from.score + self.joint_to.score

    @property
    def num(self) -> int:
        return self._num

    @property
    def name(self) -> str:
        return "{0}_to_{1}".format(self.joint_from.name, self.joint_to.name)

    @property
    def joint_from(self) -> Joint2D:
        return self._joint_from

    @property
    def joint_to(self) -> Joint2D:
        return self._joint_to

    @property
    def score(self) -> float:
        if self._score == -1:
            self._score = self.joint_from.score + self.joint_to.score / 2
        return self._score

    @property
    def is_set(self) -> bool:
        return self.joint_from.is_set and self.joint_to.is_set

    def reset(self):
        """
        Sets the limb to the default (unset) state.
        """
        self._score = -1

    def copy_from(self, other: 'Limb2D'):
        assert self.num == other.num, 'Limb numbers don\'t match'
        self._joint_from.copy_from(other.joint_from)
        self._joint_to.copy_from(other.joint_to)
        self._score = other.score

    # Serialization

    def to_dict(self):
        return {
            'num': self._num,
            'joint_from': self.joint_from.to_dict(),
            'joint_to': self.joint_to.to_dict(),
            'score': self.score
        }

    @staticmethod
    def from_dict(joint_2d_dict: Dict[str, Any]) -> 'Limb2D':
        return Limb2D(num=joint_2d_dict['num'],
                      joint_from=Joint2D.from_dict(joint_2d_dict['joint_from']),
                      joint_to=Joint2D.from_dict(joint_2d_dict['joint_to']),
                      score=float(joint_2d_dict['score']))
