class Joint2D(object):
    __slots__ = ['_num', '_name', 'x', 'y', 'score']

    @property
    def coordinates(self):
        return [self.x, self.y]

    def __init__(self, num: int, name: str, x:int = -1, y: int = -1, score: float = -1):
        """
        Data class for 2D joints
        :param num: The number of the joint in the skeleton configuration
        :param name: The name of the joint
        :param x: The X coordinate (row pixel in image)
        :param y: The Y coordinate (column pixel in image)
        :param score: The prediction score
        """
        self._num = num
        self._name = name
        self.x = x
        self.y = y
        self.score = score

    @property
    def num(self) -> int:
        return self._num

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_set(self) -> bool:
        return self.score != -1 and self.x != -1 and self.y != -1
