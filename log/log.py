import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.debug("This is a debug message")
logging.warning("Watch out!")  # will print a message to the console
logging.info("I told you so")  # will not print anything

logger = logging.getLogger("demo")
logger.info("This is a custom logger message")
logger.error("This is an error message")
logger.warning("This is a warning message")
logger.debug("This is a debug message")
