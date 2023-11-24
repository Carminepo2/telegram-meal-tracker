"""Handlers for the bot"""
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler


async def hello_callback(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    """Say hello to the user"""
    assert update.message is not None

    print(update.message.chat_id)

    await update.message.reply_text("hello")


hello_handler = CommandHandler("hello", hello_callback)
