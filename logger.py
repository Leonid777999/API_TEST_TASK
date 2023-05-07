from loguru import logger


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):

    def __init__(self, log):
        pass

    @classmethod
    def debug(cls,param):
        logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB",
                   compression="zip", colorize=True)
        return logger.debug(param)

    @classmethod
    def info(cls, param):
        logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB",
                   compression="zip", colorize=True)
        return logger.info(param)

    @classmethod
    def warning(cls, param):
        logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB",
                   compression="zip", colorize=True)
        return logger.warning(param)

    @classmethod
    def error(cls, param):
        logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB",
                   compression="zip", colorize=True)
        return logger.error(param)
