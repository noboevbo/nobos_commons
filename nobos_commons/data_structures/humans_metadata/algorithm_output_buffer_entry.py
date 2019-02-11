from typing import Any


class AlgorithmOutputBufferEntry(object):
    def __init__(self, identifier: str, algorithm_output: Any):
        self.identifier: str = identifier
        self.algorithm_output: Any = algorithm_output
