import os

from dotenv import load_dotenv

load_dotenv()


MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# Debugging: Print values to ensure they're set
print("MYSQL_USERNAME:", MYSQL_USERNAME)
print("MYSQL_PASSWORD:", MYSQL_PASSWORD)
print("MYSQL_HOST:", MYSQL_HOST)
print("MYSQL_DATABASE:", MYSQL_DATABASE)

CONFIG = {
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "SESSION_TYPE": "filesystem",
    "SQLALCHEMY_DATABASE_URI": (
        "mysql+pymysql://"
        + MYSQL_USERNAME
        + ":"
        + MYSQL_PASSWORD
        + "@"
        + MYSQL_HOST
        + "/"
        + MYSQL_DATABASE
    ),
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
}
