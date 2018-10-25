import logging

from nobos_commons.utils.file_helper import get_create_path


#TODO: Make this more useable ...

logger = logging.getLogger()

logFormatter = logging.Formatter("%(asctime)s [%(filename)s | %(funcName)s()] [%(levelname)s]  %(message)s")

logPath = get_create_path("logs") #Todo configurable
fileHandler = logging.FileHandler("{0}/{1}.log".format(r'logs', 'info'))
fileHandler.setFormatter(logFormatter)
fileHandler.setLevel(logging.ERROR)
logger.addHandler(fileHandler)

consoleFormatter = logging.Formatter("[%(funcName)s] %(message)s")
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(consoleFormatter)
consoleHandler.setLevel(logging.DEBUG)
logger.addHandler(consoleHandler)

logger.setLevel(logging.INFO)