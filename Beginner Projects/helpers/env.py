import os
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOTENV_PATH = os.path.join(BASE_DIR, ".env")


if os.path.exists(DOTENV_PATH):
    load_dotenv(DOTENV_PATH)
else:
    print("⚠️ .env not found at", DOTENV_PATH)

def get(key: str, default=None):
    return os.getenv(key, default)
