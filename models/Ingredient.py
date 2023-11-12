""" 
Ingredient model
"""


class Ingredient:
    """
    This model represents each ingredient
    """

    def __init__(self, name: int, weight: int, calories: int):
        self.name = name
        self.weight = weight
        self.calories = calories
