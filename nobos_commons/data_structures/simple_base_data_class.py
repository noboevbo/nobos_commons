from typing import TypeVar, Generic, Iterator

T = TypeVar('T')


class BaseIterablePropertyClass(Generic[T]):
    """
    This class is a base class for data classes, which only contain fields which should be accessible like a
    Ordered dictionary. So accessing via index (obj[0]), name (obj['var_name']) is possible as well as
    iterating over it (for var_name, var_value in obj).
    The implementing classes need to add their iterator return type to the BaseClass,
    e.g. ChildClass[BaseIterablePropertyClass[ReturnType]]
    The child classes should have attributes starting with a _, and a property to access each attribute
    """
    def __get_key_from_index(self, idx: int) -> str:
        return list(self.__dict__.keys())[idx]

    def __get_index_from_key(self, key: str) -> int:
        return list(self.__dict__.keys()).index('_' + key)

    def __iter__(self) -> Iterator[T]:
        return iter(self.__dict__.values())

    def __getitem__(self, key) -> T:
        if type(key) == int:
            return list(self.__dict__.values())[key]
        else:
            return self.__dict__['_' + key]

    # def __setitem__(self, key, value: T):
    #     if type(key) == int:
    #         self.__dict__[self.__get_key_from_index(key)] = value
    #     else:
    #         self.__dict__[key] = value

    def __len__(self):
        return len(self.__dict__)
