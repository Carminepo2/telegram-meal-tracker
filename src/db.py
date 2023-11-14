import datetime
import uuid
from peewee import (
    SqliteDatabase,
    Model,
    UUIDField,
    TextField,
    IntegerField,
    ForeignKeyField,
    ManyToManyField,
    DateTimeField,
)

from configs.env import ENV

db = SqliteDatabase(ENV.DATABASE, pragmas={"foreign_keys": 1})


class BaseModel(Model):
    """
    All the models that inherit from this class will be stored in the same database.
    """

    class Meta:
        database = db


class User(BaseModel):
    """
    This model represents the user of the bot
    """

    chat_id = IntegerField(primary_key=True, unique=True)
    group_chat_id = IntegerField()
    name = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)


class Food(BaseModel):
    """
    This model represents the food that the user can eat.
    """

    name = TextField(primary_key=True)
    calories = IntegerField()  # calories per 100g


class Ingredient(BaseModel):
    """
    This model represents each ingredient
    """

    id = UUIDField(primary_key=True, default=uuid.uuid4)
    food = ForeignKeyField(Food)
    weight = IntegerField()


class Meal(BaseModel):
    """
    This model represents a meal that the user has eaten.
    """

    id = UUIDField(primary_key=True, default=uuid.uuid4)
    consumer = ForeignKeyField(User, backref="meals", on_delete="CASCADE")
    ingredients = ManyToManyField(Ingredient, on_delete="CASCADE")
    timestamp = DateTimeField(default=datetime.datetime.now)


db.create_tables([Food, Meal, Ingredient, User, Meal.ingredients.get_through_model()])
