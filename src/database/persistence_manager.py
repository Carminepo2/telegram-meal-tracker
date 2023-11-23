# from database.db import Food, Group, Ingredient, Meal, User
# from utils.singleton import Singleton


# class PersistenceManager(Singleton):
#     @staticmethod
#     def add_user(chat_id: int, group_chat_id: int, name: str) -> User:
#         new_user = User.create(chat_id=chat_id, group_chat_id=group_chat_id, name=name)
#         new_user.save()
#         return new_user

#     @staticmethod
#     def get_user(chat_id: int) -> User:
#         return User.get(User.chat_id == chat_id)

#     @staticmethod
#     def get_all_users() -> list[User]:
#         return User.select()

#     @staticmethod
#     def get_all_users_in_group_chat(group_chat_id: int) -> list[User]:
#         return User.select().where(User.group_chat_id == group_chat_id)

#     @staticmethod
#     def delete_user(chat_id: int):
#         User.delete().where(User.chat_id. == chat_id).execute()

#     @staticmethod
#     def delete_all_users():
#         User.delete().execute()

#     @staticmethod
#     def delete_group_chat(group_chat_id: int):
#         User.delete().where(User.group_chat_id == group_chat_id).execute()

#     @staticmethod
#     def get_food(name: str) -> Food:
#         return Food.get(Food.name == name)

#     @staticmethod
#     def get_all_food() -> list[Food]:
#         return Food.select()

#     @staticmethod
#     def add_food(name: str, calories: int) -> Food:
#         new_food = Food.create(name=name, calories=calories)
#         new_food.save()
#         return new_food

#     @staticmethod
#     def delete_food(name: str):
#         Food.delete().where(Food.name == name).execute()

#     @staticmethod
#     def add_ingredient(food: Food, weight: int) -> Ingredient:
#         new_ingredient = Ingredient.create(food=food, weight=weight)
#         new_ingredient.save()
#         return new_ingredient

#     @staticmethod
#     def delete_ingredient(ingredient: Ingredient):
#         ingredient.delete().execute()

#     @staticmethod
#     def get_all_groups(reminder: str) -> list[Group]:
#         return Group.select().where(getattr(Group, reminder) == 1)

#     @staticmethod
#     def add_meal(consumer: User, ingredients: list[Ingredient]) -> Meal:
#         meal: Meal = Meal.create(consumer=consumer)
#         meal.save()
#         for ingredient in ingredients:
#             meal.ingredients.add(ingredient)
#         return meal
