from loguru import logger


class Logger:

    def __init__(self):

        self.add = logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB",
                              compression="zip", serialize=True, colorize=True)

    def trace(self):
        return logger.trace("TRACE")

    def debug(self):
        return logger.debug("DEBUG")

    def info(self):
        return logger.info("INFO")

    def success(self):
        return logger.success("SUCCESS")

    def warning(self):
        return logger.warning("WARNING")

    def error(self):
        return logger.error("ERROR")
    def critical(self):
        return logger.critical("CRITICAL")


