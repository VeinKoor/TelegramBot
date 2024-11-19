from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import app.keyboards as kb
from app.states import Register

router = Router()

@router.message(Command('start'))
async def ad(message: Message):
    await message.answer('Это команда start', reply_markup=kb.main)

@router.message(Command('ad'))
async def ad(message: Message):
    await message.answer('Это команда ad')

@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара:', reply_markup=kb.catalog)

@router.callback_query(F.data == '1')
async def first(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали категорию 1')

@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите имя:')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer('Введите возраст:')

@router.message(Register.age)
async def register_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer('Введите номер телефона:', reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data['name']}\nВаш возраст: {data['age']}\nВаш номер: {data['number']}')
    await state.clear()
