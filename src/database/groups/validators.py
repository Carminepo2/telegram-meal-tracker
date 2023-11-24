from pymongo.collection import Collection
from database.groups.errors import (
    GroupAlreadyExists,
    GroupNotFound,
    GroupReminderAlreadyDisabled,
    GroupReminderAlreadyEnabled,
)

from database.groups.types import Group, ReminderType


def assert_group_does_not_already_exist(group_id: int, collection: Collection[Group]):
    """Asserts that a group with the given group_id does not already exist in the database"""
    group = collection.find_one({"group_id": group_id})
    if group is not None:
        raise GroupAlreadyExists(group_id)


def assert_group_reminder_is_not_already_enabled(
    group_id: int, reminder_type: ReminderType, collection: Collection[Group]
):
    """Asserts that a given group does not already have a specific reminder enabled"""
    group = collection.find_one({"group_id": group_id})
    if group is None:
        raise GroupNotFound(group_id)
    if group[reminder_type] is True:
        raise GroupReminderAlreadyEnabled(group_id, reminder_type)


def assert_group_reminder_is_not_already_disabled(
    group_id: int, reminder_type: ReminderType, collection: Collection[Group]
):
    """Asserts that a given group does not already have a specific reminder disabled"""
    group = collection.find_one({"group_id": group_id})
    if group is None:
        raise GroupNotFound(group_id)
    if group[reminder_type] is True:
        raise GroupReminderAlreadyDisabled(group_id, reminder_type)
