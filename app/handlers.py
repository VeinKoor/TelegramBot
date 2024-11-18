from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

import app.keyboards as kb

router = Router()




@router.message(Command('start'))
async def ad(message: Message):
    await message.answer('Это команда start', reply_markup=kb.main)

@router.message(Command('ad'))
async def ad(message: Message):
    await message.answer('Это команда ad')

# @router.message()
# async def echo(message: Message):
#     await message.send_copy(message.chat.id)

