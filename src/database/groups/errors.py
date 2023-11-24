from database.groups.types import ReminderType


class GroupNotFound(Exception):
    """Raised when a group is not found in the database"""

    def __init__(self, group_id: int):
        super().__init__(f"Group with id {group_id} not found in the database")


class GroupAlreadyExists(Exception):
    """Raised when a group with the same group_id already exists in the database"""

    def __init__(self, group_id: int):
        super().__init__(f"Group with id {group_id} already exists in the database")


class GroupReminderAlreadyEnabled(Exception):
    """Raised when we are trying to activate a group reminder that is already enabled"""

    def __init__(self, group_id: int, reminder_type: ReminderType):
        super().__init__(f"{reminder_type} is already enabled for group {group_id}")


class GroupReminderAlreadyDisabled(Exception):
    """Raised when we are trying to disabled a group reminder that is already disabled"""

    def __init__(self, group_id: int, reminder_type: ReminderType):
        super().__init__(f"{reminder_type} is already disabled for group {group_id}")
