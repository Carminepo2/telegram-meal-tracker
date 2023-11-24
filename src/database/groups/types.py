from typing import Literal, TypedDict


class Group(TypedDict):
    group_id: int
    breakfast_reminder: bool
    # breakfast_reminder_time = DateTimeField()
    lunch_reminder: bool
    # lunch_reminder_time = DateTimeField()
    dinner_reminder: bool
    # dinner_reminder_time = DateTimeField()


type ReminderType = Literal["breakfast_reminder", "lunch_reminder", "dinner_reminder"]
