from .currency import *
import os
from dotenv import load_dotenv

# Always load the .env from project root
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_PATH = os.path.join(ROOT_DIR, ".env")

load_dotenv(dotenv_path=ENV_PATH)
