from typing import List, Dict, Callable


class CacheArgReplacement(object):
    __slots__ = ['func_name', 'arg_name', 'arg_replacement_func']
    func_name: str
    arg_name: str
    arg_replacement_func: Callable

    def __init__(self, func_name: str, arg_name: str, arg_replacement_func: Callable):
        """
        This CacheArgReplacements can be used to update some cached values after args changed. E.g. when files are moved
        to another directory, but remained the same you could create something like arg_replacement_func =
        str.replace(arg_value, "/some/old/path")
        The cache will look if it can find a cached version with arg /some/old/path and if so it will be moved to a new
        cache value with arg arg_value.
        :param func_name:
        :param arg_name:
        :param old_value:
        :param new_value:
        """
        self.func_name = func_name
        self.arg_name = arg_name
        self.arg_replacement_func = arg_replacement_func


class CacheConfig(object):
    __slots__ = ['cache_enabled', 'cache_dir', 'func_names_to_reload', 'str_args_replacement_dict', 'reload_all']

    def __init__(self, cache_dir: str, func_names_to_reload: List[str] = None,
                 str_args_replacements: List[CacheArgReplacement] = None,
                 reload_all: bool = False, cache_enabled: bool = True):
        self.cache_dir = cache_dir
        self.func_names_to_reload = func_names_to_reload
        if self.func_names_to_reload is None:
            self.func_names_to_reload = []
        self.reload_all = reload_all
        self.cache_enabled = cache_enabled
        self.str_args_replacement_dict = self.__get_str_arg_replacement_dict(str_args_replacements)

    @staticmethod
    def __get_str_arg_replacement_dict(str_args_replacements: List[CacheArgReplacement]) -> Dict[str, List[CacheArgReplacement]]:
        str_args_replacement_dict: Dict[str, List[CacheArgReplacement]] = {}
        if str_args_replacements is None:
            return str_args_replacement_dict
        for str_args_replacement in str_args_replacements:
            if str_args_replacement.func_name not in str_args_replacement_dict.keys():
                str_args_replacement_dict[str_args_replacement.func_name] = []
            str_args_replacement_dict[str_args_replacement.func_name].append(str_args_replacement)
        return str_args_replacement_dict
