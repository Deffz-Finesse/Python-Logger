from logger import get_logger

# Initialize the logger for this module
logger = get_logger("Example Module")

logger.info("Everything is working.")
logger.debug("Debugging stuff...")
logger.warning("Watch out!")
logger.error("Something went wrong.")
logger.critical("This is critical!")