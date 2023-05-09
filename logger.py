from loguru import logger


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):

    def __init__(self):
        self. logger = logger
        self.logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB",
                   compression="zip", colorize=True)


    def debug(self,param):
        return self.logger.debug(param)


    def info(self, param):
        return self.logger.info(param)


    def warning(cls, param):
        return logger.warning(param)


    def error(cls, param):
        return logger.error(param)
