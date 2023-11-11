import os
from dotenv import load_dotenv


class Config:
    """Contains all the necessary configuration variables for the application"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        load_dotenv()

    @property
    def bot_token(self) -> str:
        """Returns the bot token that is used to authenticate with the Telegram API"""
        return self.__get_env("BOT_TOKEN")

    def __get_env(self, key: str) -> str:
        """Returns the value of the environment variable with the given key"""
        value = os.getenv(key)
        assert value is not None, f"{key} environment variable must be set"
        return value


config = Config()
