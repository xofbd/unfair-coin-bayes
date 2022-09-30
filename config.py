import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = "secret key"


class ConfigProd(Config):
    FLASK_ENV = "production"
    SECRET_KEY = os.getenv("SECRET_KEY")


class ConfigDev(Config):
    FLASK_ENV = "development"


class ConfigTesting(Config):
    FLASK_ENV = "testing"
    TESTING = True
    WTF_CSRF_ENABLED = False
