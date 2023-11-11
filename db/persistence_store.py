import sqlite3

from models.Meal import Meal
from utils.singleton import Singleton


class PersistenceStore(Singleton):
    """
    This class is responsible for storing and retrieving meals from the database.
    """

    def __init__(self):
        self.db_path = "db/meal_tracker.db"
        self.db = sqlite3.connect(self.db_path)
        self.cursor = self.db.cursor()

        self.__create_tables()

    def add_meal(self, meal: Meal):
        """
        Adds a meal to the database
        """

        self.cursor.execute(
            "INSERT INTO meals (user_chat_id, content, calories) VALUES (?, ?, ?)",
            (meal.user_chat_id, meal.content, meal.calories),
        )
        self.db.commit()

    def __create_tables(self):
        """
        Initializes the database tables
        """
        with open(
            "db/sql/create_tables.sql", "r", encoding="utf-8"
        ) as create_table_file:
            self.cursor.executescript(create_table_file.read())
            self.db.commit()


persistence_store = PersistenceStore()
