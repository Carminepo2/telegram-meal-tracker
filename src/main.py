#!/usr/bin/env python3.12

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
from configs.env import ENV

from handlers import hello_handler
from services.persistence_manager import PersistenceManager


def main():
    """Starts the bot"""

    app = ApplicationBuilder().token(ENV.BOT_TOKEN).build()

    app.add_handler(hello_handler)

    logger.info("Starting polling...")
    # app.run_polling()

    carmine = PersistenceManager.add_user(chat_id=1, group_chat_id=1, name="Carmine")
    # matteucci = PersistenceManager.add_user(
    #     chat_id=2, group_chat_id=1, name="Matteucci"
    # )

    # logger.info(carmine.name)
    # logger.info(matteucci.name)

    pasta = PersistenceManager.add_food(name="Pasta", calories=100)
    pizza = PersistenceManager.add_food(name="Pizza", calories=200)

    # pasta = PersistenceManager.get_food(name="Pasta")
    # pizza = PersistenceManager.get_food(name="Pizza")

    ingredient1 = PersistenceManager.add_ingredient(food=pasta, weight=100)
    ingredient2 = PersistenceManager.add_ingredient(food=pizza, weight=200)

    # carmine = PersistenceManager.get_user(chat_id=1)

    meal = PersistenceManager.add_meal(
        consumer=carmine, ingredients=[ingredient1, ingredient2]
    )
    # meal.ingredients

    # logger.info(meal.consumer.name)


if __name__ == "__main__":
    main()
