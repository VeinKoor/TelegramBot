from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer('Hi')
