from dotenv import dotenv_values

config = dotenv_values(".env")

CONFIG = {
    "SECRET_KEY": config["SECRET_KEY"],
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "SESSION_TYPE": "filesystem",
    "SQLALCHEMY_DATABASE_URI":f"mysql+pymysql://{config["MYSQL_USERNAME"]}:{config["MYSQL_PASSWORD"]}@{config['MYSQL_HOST']}/{config['MYSQL_DATABASE']}",
    "SQLALCHEMY_TRACK_MODIFICATIONS":False,
}
