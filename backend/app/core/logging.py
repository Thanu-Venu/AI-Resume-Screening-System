import logging
import os

from app.core.config import settings

def configure_logging() -> None:
    #create logs directory if it doesnt exist
    os.makedirs("logs" , exist_ok=True)

    #convert "INFO" into logging.INFO
    log_level = getattr(logging,settings.log_level.upper())

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("logs/application.log"),
        ],
    )