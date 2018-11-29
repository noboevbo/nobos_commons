from nobos_commons.data_structures.skeletons.joint_2d import Joint2D


class Limb2D(object):
    def __init__(self, num: int, joint_from: Joint2D, joint_to: Joint2D, score: int = -1):
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
        self.score: float = score

    @property
    def matched_score(self) -> float:
        return self.score + self.joint_from.score + self.joint_to.score

    @property
    def num(self) -> int:
        return self._num

    @property
    def joint_from(self) -> Joint2D:
        return self._joint_from

    @property
    def joint_to(self) -> Joint2D:
        return self._joint_to

    @property
    def is_set(self) -> bool:
        return self.score != -1

    def copy_from(self, other: 'Limb2D'):
        assert self.num == other.num, 'Limb numbers don\'t match'
        self._joint_from.copy_from(other.joint_from)
        self._joint_to.copy_from(other.joint_to)
        self.score = other.score
