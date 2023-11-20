from aiogram import Router, F, types
from aiogram.filters import Command
from db import queries
from pathlib import Path
# from main import bot

car_router = Router()

img = Path('image')


@car_router.message(Command('get'))
async def get(message: types.Message):
    cars = queries.get_products()
    for i in cars:
        file = types.FSInputFile(i[3])
        await message.answer_photo(photo=file, caption=(f'Марка: {i[1]} \n \n '
                                                        f'Цена: {i[2]}'))
