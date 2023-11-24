from database.db import db
from database.groups.errors import GroupNotFound
from database.groups.types import Group, ReminderType
from database.groups.validators import (
    assert_group_does_not_already_exist,
    assert_group_reminder_is_not_already_enabled,
    assert_group_reminder_is_not_already_disabled,
)


class GroupsService:
    @staticmethod
    def get_group(group_id: int) -> Group:
        result = db.groups.find_one({"group_id": group_id})
        if result is None:
            raise GroupNotFound(group_id)
        return result

    @staticmethod
    def get_all_groups():
        return db.groups.find({})

    @staticmethod
    def get_all_groups_with_active_reminder(reminder_type: ReminderType):
        return db.groups.find({reminder_type: True})

    @staticmethod
    def create_group(group_id: int):
        assert_group_does_not_already_exist(group_id, db.groups)

        return db.groups.insert_one(
            Group(
                group_id=group_id,
                breakfast_reminder=True,
                lunch_reminder=True,
                dinner_reminder=True,
            )
        )

    @staticmethod
    def enable_group_reminder(group_id: int, reminder_type: ReminderType):
        assert_group_reminder_is_not_already_enabled(group_id, reminder_type, db.groups)

        return db.groups.update_one(
            {"group_id": group_id}, {"$set": {reminder_type: True}}
        )

    @staticmethod
    def disable_group_reminder(group_id: int, reminder_type: ReminderType):
        assert_group_reminder_is_not_already_disabled(
            group_id, reminder_type, db.groups
        )

        return db.groups.update_one(
            {"group_id": group_id}, {"$set": {reminder_type: False}}
        )

    @staticmethod
    def delete_group(group_id: int):
        return db.groups.delete_one({"group_id": group_id})

    @staticmethod
    def delete_all_groups():
        return db.groups.delete_many({})
