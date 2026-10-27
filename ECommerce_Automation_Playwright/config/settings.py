import os
from pathlib import Path

from dotenv import load_dotenv


# Locate the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load environment variables from the project root
load_dotenv(PROJECT_ROOT / ".env")

# Read application configuration
BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.saucedemo.com"
).rstrip("/")

DEFAULT_TIMEOUT_MS = int(
    os.getenv("DEFAULT_TIMEOUT_MS", "10000")
)