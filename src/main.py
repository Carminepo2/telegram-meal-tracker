#!/usr/bin/env python3.12

"""
This bot is supposed to be used to track our meals through the day.
This is the main reason this bot exists, but it may be used for other purposes as well.

Time will tell.

The bot has a list of groups that it is part of. 
In each group the bot sends a reminder for breakfast, lunch and dinner and sometimes randomly asks for a snack.
The reminders can be disabled by the users in the group.

"""

__author__ = "Carmine e Matteucci"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger
from telegram.ext import ApplicationBuilder
from configs.env import ENV

from handlers import hello_handler


def main():
    """Starts the bot"""

    app = ApplicationBuilder().token(ENV.BOT_TOKEN).build()

    # meal_reminder_manager = MealReminderManager(app.job_queue)
    # meal_reminder_manager.start_reminder_jobs()

    app.add_handler(hello_handler)

    logger.info("Starting polling...")
    app.run_polling()


if __name__ == "__main__":
    main()
