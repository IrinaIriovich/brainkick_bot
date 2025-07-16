from aiogram import Dispatcher, types
from logic_tasks import get_daily_task
from google_sheets import record_response


def setup_handlers(dp: Dispatcher):
    @dp.message(commands=["start"])
    async def send_welcome(message: types.Message):
        await message.answer("Привет! Готов к ежедневному заданию? Напиши /день")

    @dp.message(commands=["день"])
    async def send_daily_task(message: types.Message):
        task = get_daily_task()
        await message.answer(task["question"], reply_markup=task["reply_markup"])

    @dp.callback_query()
    async def handle_response(callback_query: types.CallbackQuery):
        data = callback_query.data
        await callback_query.message.edit_reply_markup()  # remove buttons
        record_response(callback_query.from_user.id, data)
        await callback_query.answer("Ответ получен!")