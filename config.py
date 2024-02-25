from dotenv import dotenv_values

config = dotenv_values(".env")

CONFIG = {
    "SECRET_KEY": config["SECRET_KEY"],
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "SESSION_TYPE": "filesystem",
}
