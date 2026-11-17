import os
from pathlib import Path
from dotenv import load_dotenv

# Locate the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Load environment variables from the project root
load_dotenv(PROJECT_ROOT / ".env")

# Read application configuration
VALID_USERNAME = os.getenv("VALID_USERNAME")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")

