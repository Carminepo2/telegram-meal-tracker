import random
from telegram.ext import JobQueue, CallbackContext
from configs.constants import (
    BREAKFAST_REMINDER_TIME,
    LUNCH_REMINDER_TIME,
    DINNER_REMINDER_TIME,
    SNACK_1_REMINDER_TIME,
    SNACK_2_REMINDER_TIME,
    SNACK_RANDOM_INDEX,
)
from database.groups import GroupsService
from utils.singleton import Singleton


class MealReminderManager(Singleton):
    def __init__(self, job_queue: JobQueue | None, groups_service: GroupsService):
        assert (
            job_queue is not None
        ), "Job queue is None, install it with `pip install python-telegram-bot[job_queue]`"
        self.job_queue = job_queue
        self.groups_service = groups_service

    def start_reminder_jobs(self):
        self.job_queue.run_daily(self.send_breakfast_reminder, BREAKFAST_REMINDER_TIME)
        self.job_queue.run_daily(self.send_lunch_reminder, LUNCH_REMINDER_TIME)
        self.job_queue.run_daily(self.send_dinner_reminder, DINNER_REMINDER_TIME)

        self.job_queue.run_daily(self.send_snacks_reminder, SNACK_1_REMINDER_TIME)
        self.job_queue.run_daily(self.send_snacks_reminder, SNACK_2_REMINDER_TIME)

    async def send_breakfast_reminder(self, _context: CallbackContext):
        groups = self.groups_service.get_all_groups_with_active_reminder(
            "breakfast_reminder"
        )
        for group in groups:
            print(f"Sending breakfast reminder to group {group.group_id}")

    async def send_lunch_reminder(self, _context: CallbackContext):
        groups = self.groups_service.get_all_groups_with_active_reminder(
            "lunch_reminder"
        )
        for group in groups:
            print(f"Sending lunch reminder to group {group.group_id}")

    async def send_dinner_reminder(self, _context: CallbackContext):
        groups = self.groups_service.get_all_groups_with_active_reminder(
            "dinner_reminder"
        )
        for group in groups:
            print(f"Sending dinner reminder to group {group.group_id}")

    async def send_snacks_reminder(self, _context: CallbackContext):
        groups = self.groups_service.get_all_groups()
        for group in groups:
            should_send_snack = random.random() < SNACK_RANDOM_INDEX
            if not should_send_snack:
                continue
            print(f"Sending snack reminder to group {group.group_id}")
