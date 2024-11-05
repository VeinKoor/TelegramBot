import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import router

async def main():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage()) # все данные бота которые не сохраняются в БД будут стёрты при перезапуске
    dp.include_router(router) # подключаем все обработчики
    await bot.delete_webhook(drop_pending_updates=True) # бот не будет читать сообщения, которые писали при перезапуске
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())