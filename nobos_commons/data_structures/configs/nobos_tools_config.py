from nobos_commons.data_structures.configs.cache_config import CacheConfig


class NobosToolsConfig(object):
    slots = ["cache_config"]

    cache_config: CacheConfig

    def __init__(self, cache_config: CacheConfig):
        self.cache_config = cache_config
