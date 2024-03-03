import os

from dotenv import load_dotenv

# Load the stored environment variables
load_dotenv()

# -------- DataBase settings -------- #
DATABASE = {
    "DB_URL": "sqlite://database.db",
    "GENERATE_SCHEMAS": True,
    "MODULES": {
        "models": [
            "user.models"
        ],
    },
}
# -------- DataBase settings -------- #

# -------- JWT settings -------- #
ALGORITHM = "HS256"
JWT_SECRET_KEY = "secret"
TOKEN_EXPIRE = 1 * 60 * 60 * 24 * 30  # 1 month
# -------- JWT settings -------- #
