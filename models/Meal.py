""" 
Meal model
"""
import uuid


class Meal:
    """
    This model represents a meal that the user has eaten.
    """

    def __init__(self, user_chat_id: str, content: str, calories: int):
        self.id = uuid.uuid4()
        self.user_chat_id = user_chat_id
        self.content = content
        self.calories = calories
