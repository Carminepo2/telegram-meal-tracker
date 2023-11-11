import os
from dotenv import load_dotenv

from utils.singleton import Singleton


class Env(Singleton):
    """Contains all the env variables"""

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


env = Env()
