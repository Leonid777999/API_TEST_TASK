from loguru import logger

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation= "10 KB", compression="zip",
           serialize=True, colorize=True)

logger.trace("TRACE")
logger.debug("DEBUG")
logger.info("INFO")
logger.success("SUCCESS")
logger.warning("WARNING")
logger.error("ERROR")
logger.critical("CRITICAL")

