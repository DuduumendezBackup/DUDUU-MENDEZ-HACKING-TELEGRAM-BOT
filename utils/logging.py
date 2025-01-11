import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            RotatingFileHandler("bot.log", maxBytes=5 * 1024 * 1024, backupCount=2),
            logging.StreamHandler(),
        ],
    )
    logger = logging.getLogger(__name__)
    return logger