import logging
from pathlib import Path

#setting the log file path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "automation.log"

#Creating the logger
logger = logging.getLogger("ECommerce-Automation Framework")
logger.setLevel(logging.INFO)

#Setting the format for the logger
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s",datefmt="%d-%b-%y %H:%M:%S")

#creating file handlers
file_handler = logging.FileHandler(LOG_FILE,mode="w",encoding="utf-8")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)

#Console handlers
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)

#Adding the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
