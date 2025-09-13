from . import currency

import os
from dotenv import load_dotenv

# Figure out project root (two levels up from helpers)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_PATH = os.path.join(BASE_DIR, ".env")

# Load .env if it exists
if os.path.exists(DOTENV_PATH):
    load_dotenv(DOTENV_PATH)
