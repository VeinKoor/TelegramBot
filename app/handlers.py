from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import app.keyboards as kb
import app.database.requests as rq


router = Router()

@router.message(Command('start'))
async def ad(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в магазин кроссовок!', reply_markup=kb.main)


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара: ', reply_markup=await kb.categories())


@router.callback_query(F.data.startswitch('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите товар по категории', reply_markup=await kb.items(callback.data.split('_')[1]))

