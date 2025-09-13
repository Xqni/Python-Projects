import os
from dotenv import load_dotenv

# folder/       <--- assuming you clone the repo inside of this folder
# ├───Beginner Projects/
# |   |
# |   ├───convproj/
# |   │   └───tests/
# |   │   
# |   └───helpers
# └───.env      <--- put your env vars here

# Assumes you have above file/dir structure
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOTENV_PATH = os.path.join(BASE_DIR, ".env")


if os.path.exists(DOTENV_PATH):
    load_dotenv(DOTENV_PATH)
else:
    # if you see this, check the file/dir structure above
    print("⚠️ .env not found at", DOTENV_PATH)

def get(key: str, default=None):
    return os.getenv(key, default)
