import collections
import hashlib
import inspect
import json
import os
import pickle
import re
import shutil
import sys
from typing import Callable, List, Any

from nobos_commons.data_structures.configs.cache_config import CacheConfig
from nobos_commons.tools.decorators.timing_decorator import stopwatch
from nobos_commons.tools.log_handler import logger
from nobos_commons.utils.file_helper import get_create_path


class __Cache(object):
    __slots__ = ['func_cache_dir', 'func_cache_dir_path', 'func', 'cache_config', 'is_method', 'replacement_args', 'arg_names']

    __cache_columns: List[str] = ['func_call_hash', 'func_name', 'func_code', 'func_args', 'func_result',
                                  'date_created']

    def __init__(self, func: Callable, cache_config: CacheConfig):
        """
        Cache decorator which currently supports functions with base type, dictionary, list and lambda parameters
        :param func:
        """
        self.func = func
        self.cache_config = cache_config
        try:
            self.func_cache_dir = self.get_function_hash()
        except OSError as err:
            print("OS Error, probably not possible to retrieve source code. Disable cache. Details: '{}'".format(err))
            self.cache_config.cache_enabled = False
            return
        self.is_method = self.__is_method(self.func)
        self.func_cache_dir_path = get_create_path(os.path.join(self.cache_config.cache_dir, self.func_cache_dir))
        self.arg_names = list(inspect.signature(self.func).parameters.keys())
        self.replacement_args = None
        if self.func.__name__ in self.cache_config.str_args_replacement_dict.keys():
            self.replacement_args = self.cache_config.str_args_replacement_dict[self.func.__name__]

    def get_arg_replaced_cache_value(self, cache_file_path: str,  *args):
        old_args = list(args)
        for replacement_arg in self.replacement_args:
            if replacement_arg.arg_name in self.arg_names:
                arg_index = self.arg_names.index(replacement_arg.arg_name)
            else:
                raise ValueError("replacement_arg {0} for function {1} is not in function signature".format(
                    replacement_arg.arg_name, self.func.__name__))
            arg_value = args[arg_index]
            old_args[arg_index] = replacement_arg.arg_replacement_func(arg_value)
        old_args = tuple(old_args)
        old_cache_file_path = self.__get_cache_file_path(*old_args)
        old_cached_value = self.__get_cached_value(old_cache_file_path)

        if old_cached_value is None:
            return None

        shutil.move(old_cache_file_path, cache_file_path)
        logger.info('Moved cache file \'{}\' to \'{}\''.format(old_cache_file_path, cache_file_path))
        return old_cached_value

    def get_args_hash(self, *args) -> str:
        arg_hashes: str = ''
        start = 1 if self.is_method else 0
        for i in range(start, len(args)):
            arg = args[i]
            if isinstance(arg, collections.Hashable):
                if isinstance(arg, str):
                    arg_hashes = "{}_{}".format(arg_hashes, hashlib.sha256(bytes(arg.encode('utf-8'))).hexdigest())
                elif callable(arg):  # is a function, TODO: Mabye use the parameters + func_path as str and hash this
                    raise NotImplementedError(
                        "Type {} is not supported for caching because it is not hashable".format(type(arg)))
                else: # TODO: OBJS?
                    arg_hashes = "{}_{}".format(arg_hashes, hashlib.sha256(bytes(arg)).hexdigest())
            else:
                if isinstance(arg, dict) or isinstance(arg, list):
                    arg_hashes = "{}_{}".format(arg_hashes, hashlib.sha256(
                        json.dumps(arg, sort_keys=True).encode('utf-8')).hexdigest())
                else:
                    raise NotImplementedError(
                        "Type {} is not supported for caching because it is not hashable".format(type(arg)))
        return hashlib.sha256(arg_hashes.encode("utf-8")).hexdigest()

    def get_function_hash(self) -> str:
        func_source = inspect.getsource(self.func)
        func_source = re.sub("@cache\(.*\)\\n", '', func_source)  # remove @cache decorator from func code
        function_hashes = "{}_{}".format(self.func.__name__,
                                         hashlib.sha256(func_source.encode('utf-8')).hexdigest())
        return hashlib.sha256(bytes(function_hashes.encode('utf-8'))).hexdigest()

    def __get_cache_file_path(self, *args) -> str:
        arg_hash = self.get_args_hash(*args)
        func_hash = self.get_function_hash()
        func_call_hashes = "{}_{}".format(func_hash, arg_hash)
        func_call_hash = hashlib.sha256(bytes(func_call_hashes.encode('utf-8'))).hexdigest()

        return os.path.join(self.func_cache_dir_path, func_call_hash)

    def __get_cached_value(self, cache_file_path: str) -> Any:
        if (self.cache_config.reload_all or self.func.__name__ in self.cache_config.func_names_to_reload) and \
                os.path.exists(cache_file_path):
            logger.info('Deleted cache file \'{}\''.format(cache_file_path))
            os.remove(cache_file_path)
        if os.path.exists(cache_file_path):
            try:
                cache_value = pickle.load(open(cache_file_path, 'rb'))
                logger.info('Loaded {} results from cache file \'{}\''.format(self.func.__name__, cache_file_path))
                return cache_value
            except:
                os.remove(cache_file_path)
        return None

    @stopwatch
    def __call__(self, *args, **kwargs):
        """
        Checks if a func result is already cached, if yes it's returned if not the func will be executed and the
        result will be saved to a cache file
        :param func: The function which produces the result
        :param cache_file_path: The cache file path
        :param reload: If a cached file exists it should be updated
        :return: The requested content, either retrieved from cache or calculated and saved to cache
        """
        if not self.cache_config.cache_enabled:
            logger.info('Cache disabled for {}'.format(self.func.__name__))
            return self.func(*args, **kwargs)
        if sys.version_info[0] == 2:
            logger.info(
                'Load {} from function, because caching is disabled or incompatible!'.format(self.func.__name__))
            return self.func(*args, **kwargs)  # pickle bug in Python2 for large datasets

        cache_file_path = self.__get_cache_file_path(*args)
        if self.replacement_args is not None:
            cached_value = self.get_arg_replaced_cache_value(cache_file_path, *args)
        else:
            cached_value = self.__get_cached_value(cache_file_path)

        if cached_value is not None:
            return cached_value

        result = self.func(*args, **kwargs)  # **kwargs

        pickle.dump(result, open(cache_file_path, 'wb'), protocol=4)
        logger.info('Created cache file for {} in \'{}\''.format(self.func.__name__, cache_file_path))
        return result

    def __get__(self, obj, objtype):
        """Support instance methods."""
        import functools
        return functools.partial(self.__call__, obj)

    @staticmethod
    def __is_method(func):
        spec = inspect.signature(func)
        if len(spec.parameters) > 0:
            if list(spec.parameters.keys())[0] == 'self':
                return True
        return False


def cache(cache_config: CacheConfig):
    def wrapper(func):
        return __Cache(func, cache_config)

    return wrapper
