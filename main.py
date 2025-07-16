import asyncio
from handlers import setup_handlers
from utils import bot, dp


async def main():
    setup_handlers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())