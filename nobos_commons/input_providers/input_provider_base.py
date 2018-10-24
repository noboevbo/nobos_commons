from typing import Any


class InputProviderBase(object):
    def get_data(self) -> Any:
        raise NotImplementedError

