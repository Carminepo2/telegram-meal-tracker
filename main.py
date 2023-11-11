#!/usr/bin/env python

"""
This bot is supposed to be used to track our meals through the day.
This is the main reason this bot exists, but it may be used for other purposes as well.

Time will tell.
"""

__author__ = "Carmine e Matteucci"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger
from telegram.ext import ApplicationBuilder

from config import config
from handlers import hello_handler


def main():
    """Starts the bot"""

    app = ApplicationBuilder().token(config.bot_token).build()

    app.add_handler(hello_handler)

    logger.info("Starting polling...")
    app.run_polling()


if __name__ == "__main__":
    main()
