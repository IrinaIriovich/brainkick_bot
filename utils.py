import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"), parse_mode=ParseMode.HTML)
dp = Dispatcher()