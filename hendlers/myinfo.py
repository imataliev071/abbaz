from aiogram import Router, types
from aiogram.filters import Command

myinfo_ruter = Router()


@myinfo_ruter.message(Command('myinfo'))  # фильтр
async def myinfo(message: types.Message):
    await message.answer(
        f'Ваш id: {message.from_user.id} '
        f'\nВаше имя: {message.from_user.first_name} '
        f'\nВаш user name: {message.from_user.username}'
    )
