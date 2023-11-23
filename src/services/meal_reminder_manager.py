from telegram.ext import JobQueue, CallbackContext
from configs.constants import (
    BREAKFAST_REMINDER_TIME,
    LUNCH_REMINDER_TIME,
    DINNER_REMINDER_TIME,
)
from database.db import Group
from utils.singleton import Singleton


class MealReminderManager(Singleton):
    def __init__(self, job_queue: JobQueue | None):
        if job_queue is None:
            raise Exception(
                "Job queue is None, install it with `pip install python-telegram-bot[job_queue]`"
            )
        self.job_queue = job_queue

    def start_reminder_jobs(self):
        print("Starting reminder jobs")
        self.job_queue.run_daily(self.send_breakfast_reminder, BREAKFAST_REMINDER_TIME)
        self.job_queue.run_daily(self.send_lunch_reminder, LUNCH_REMINDER_TIME)
        self.job_queue.run_daily(self.send_dinner_reminder, DINNER_REMINDER_TIME)
        self.job_queue.run_daily(self.send_snacks_reminder, DINNER_REMINDER_TIME)

    async def send_breakfast_reminder(self, context: CallbackContext):
        # groups: list[Group] = Group.select().where(Group.breakfast_reminder == 1)
        # for group in groups:
        print("Sending breakfast reminder")
        context.bot.send_message(
            chat_id=4036421530,
            text="It's time for breakfast!",
        )

    async def send_lunch_reminder(self, context: CallbackContext):
        pass

    async def send_dinner_reminder(self, context: CallbackContext):
        pass

    async def send_snacks_reminder(self, context: CallbackContext):
        pass
