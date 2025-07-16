import json
import random
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_daily_task():
    with open("daily_tasks.json", "r", encoding="utf-8") as f:
        tasks = json.load(f)
    task = random.choice(tasks)
    keyboard = InlineKeyboardMarkup().add(InlineKeyboardButton("Показать ответ", callback_data=task["answer"]))
    return {"question": task["question"], "reply_markup": keyboard}