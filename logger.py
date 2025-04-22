# src/lib/logger.py

import os
import logging
from dotenv import load_dotenv
from colorlog import ColoredFormatter
from logging.handlers import RotatingFileHandler

# Load environment variables
load_dotenv()

# Environment Config
LOG_DIR = "logs"
ENV = os.getenv("ENV")
LOG_LEVEL = os.getenv("LOG_LEVEL").upper()
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Ensure logs directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Formatter - Console and File (No color in file logs)
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FORMAT = "%(asctime)s [%(name)s] - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"

# Colored Formatter for console
COLORED_FORMAT = ColoredFormatter(
    "%(log_color)s%(asctime)s [%(name)s] - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    datefmt=DATE_FORMAT,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # Set global log level
    logger.setLevel(LOG_LEVEL)

    # Console Handler (Always enabled)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(COLORED_FORMAT)
    console_handler.setLevel(LOG_LEVEL)
    logger.addHandler(console_handler)

    # File Handler with rotation (5MB x 5 backups)
    file_handler = RotatingFileHandler(
        LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5
    )
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT))
    file_handler.setLevel(LOG_LEVEL)
    logger.addHandler(file_handler)

    # Disable propagation if needed
    logger.propagate = False

    return logger