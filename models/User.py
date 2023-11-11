""" 
User model
"""


class User:
    """
    This model represents the user of the bot
    """

    def __init__(self, chat_id: int, name: str):
        self.chat_id = chat_id
        self.name = name
