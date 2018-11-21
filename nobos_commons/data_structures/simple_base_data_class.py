class SimpleBaseDataClass(object):
    """
    This class is a base class for data classes, which only contain fields which should be accessible like a
    Ordered dictionary. So accessing via index (obj[0]), name (obj['var_name']) is possible as well as
    iterating over it (for var_name, var_value in obj)
    """
    def __get_key_from_index(self, idx: int):
        return list(self.__dict__.keys())[idx]

    def __iter__(self):
        return iter(self.__dict__.items())

    def __getitem__(self, key):
        if type(key) == int:
            return list(self.__dict__.values())[key]
        else:
            return self.__dict__[key]

    def __setitem__(self, key, value):
        if type(key) == int:
            self.__dict__[self.__get_key_from_index(key)] = value
        else:
            self.__dict__[key] = value

    def __len__(self):
        return len(self.__dict__)
