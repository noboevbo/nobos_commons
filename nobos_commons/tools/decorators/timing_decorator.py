import time

from nobos_commons.tools.log_handler import logger


def stopwatch(func):
    def timed(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()

        logger.info('%r  %2.2f ms' % (func.__name__, (te - ts) * 1000))
        return result

    return timed