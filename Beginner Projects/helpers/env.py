"""
This file loads .env file to be usable by other modules and packages.

Keep in mind the .env file should be 3 levels up from the current file
<your own folder>/Beginner Projects/helpers/env.py

::Usage::
import helper.env as env   <--- currently only works in Beginner Projects directory

print(env.get("API_KEY))
^ should print your API KEY stored inside .env file
"""


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
