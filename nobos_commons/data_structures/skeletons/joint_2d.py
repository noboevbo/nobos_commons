from typing import Dict, Any

from nobos_commons.data_structures.skeletons.joint_visibility import JointVisibility


class Joint2D(object):
    __slots__ = ['_num', '_name', 'x', 'y', 'score', 'visibility']

    def __init__(self, num: int = -1, name: str = None, x: int = -1, y: int = -1, score: float = -1,
                 visibility: JointVisibility = JointVisibility.VISIBLE):
        """
        Data class for 2D joints
        :param num: The number of the joint in the skeleton configuration
        :param name: The name of the joint
        :param x: The X coordinate (row pixel in image)
        :param y: The Y coordinate (column pixel in image)
        :param score: The prediction score
        :param visibility: The visibility of the joint (Usually only used in datasets for training purpose)
        """
        self._num: int = num
        self._name: str = name
        self.x: int = x
        self.y: int = y
        self.score: float = score
        self.visibility: JointVisibility = visibility

    def copy_from(self, other: 'Joint2D', allow_different_num: bool = False, allow_different_name: bool = False):
        if not allow_different_num:
            assert other.is_unassigned_joint or self.num == other.num, 'Joint numbers don\'t match'
        if not allow_different_name:
            assert other.is_unassigned_joint or self.name == other.name, 'Joint names don\'t match'
        self.x = other.x
        self.y = other.y
        self.score = other.score
        self.visibility = other.visibility

    @property
    def num(self) -> int:
        return self._num

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_set(self) -> bool:
        return self.score != -1 and self.x != -1 and self.y != -1

    @property
    def is_unassigned_joint(self) -> bool:
        return self.num == -1 and self.name is None

    def reset(self):
        """
        Sets the joint to the default (unset) state.
        """
        self.x = -1
        self.y = -1
        self.score = -1

    # Serialization

    def to_dict(self):
        return {
            'num': self._num,
            'name': self._name,
            'x': self.x,
            'y': self.y,
            'score': self.score,
            'visibility': self.visibility.name
        }

    @staticmethod
    def from_dict(joint_2d_dict: Dict[str, Any]) -> 'Joint2D':
        return Joint2D(num=joint_2d_dict['num'],
                       name=joint_2d_dict['name'],
                       x=int(joint_2d_dict['x']),
                       y=int(joint_2d_dict['y']),
                       score=float(joint_2d_dict['score']),
                       visibility=JointVisibility(joint_2d_dict['visibility']))
