from loguru import logger


class Logger:

    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Logger, cls).__new__(cls)
        return cls.__instance



logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB",
                              compression="zip", serialize=True, colorize=True)

logger.trace("TRACE")
logger.debug("DEBUG")
logger.info("INFO")
logger.success("SUCCESS")
logger.warning("WARNING")
logger.error("ERROR")
logger.critical("CRITICAL")


