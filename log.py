from loguru import logger



class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):

    def __init__(self):
        self.logger = logger
        self.logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB",
                        compression="zip", colorize=True, mode="w")

    def debug(self, message: str):
        """

        :return:
        """
        return self.logger.debug(message)

    def info(self, message: str):
        """

        :return:
        """
        return self.logger.info(message)

    def warning(self, message: str):
        """

        :return:
        """
        return self.logger.warning(message)

    def error(self, message: str):
        """

        :return:
        """
        return self.logger.error(message)





