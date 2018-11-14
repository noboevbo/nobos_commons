from typing import List

from nobos_commons.tools.decorators.cache_decorator import cache

from nobos_commons.data_structures.configs.cache_config import CacheConfig, CacheArgReplacement

# replacement_test: List[CacheArgReplacement] = []
replacement_test: List[CacheArgReplacement] = [
    CacheArgReplacement("test", "b", lambda arg_value: arg_value.replace("/media/disks/beta/2", "/media/disks/beta/1"))]


@cache(CacheConfig(cache_dir="/media/disks/beta/cache",
                   func_names_to_reload=[],
                   str_args_replacements=replacement_test,
                   reload_all=False))
def test2(a, b, c):
    x = a
    y = b
    z = c
    return 1


class Test:
    @cache(CacheConfig(cache_dir="/media/disks/beta/cache",  func_names_to_reload=[],  str_args_replacements=replacement_test, reload_all=False))
    def test(self, a, b, c):
        x = a
        y = b
        z = c
        return 1


#test2(1, 2, 3)
v = Test()
v.test("123", "/media/disks/beta/2", lambda x: x - 5)
# v.test("123", "/media/disks/beta/1", lambda x: x - 5)
# v.test("123", "/media/disks/beta/1", lambda x: x - 5)
# v.test("123", "/media/disks/beta/1", lambda x: x - 5)
# v.test("12", "/media/disks/beta/1", lambda x: x - 5)
# v.test("123", "/media/disks/beta/1", lambda x: x - 5)