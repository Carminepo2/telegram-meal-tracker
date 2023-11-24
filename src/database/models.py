from typing import TypedDict
from bson import ObjectId


class User(TypedDict):
    """
    This model represents the user of the bot
    """

    telegram_id: int
    name: str
    created_at: str


class Food(TypedDict):
    name: str
    calories: int  # calories per 100g


class Ingredient(TypedDict):
    food_id: str
    weight: int


class Meal(TypedDict):
    id: str
    consumer_id: ObjectId
    ingredients: list[Ingredient]
    timestamp: str
