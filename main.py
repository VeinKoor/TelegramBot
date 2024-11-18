import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command

from app.handlers import router
from config import TOKEN


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    print("Бот запущен")

    dp.include_router(router)
    await dp.start_polling(bot)


asyncio.run(main())
