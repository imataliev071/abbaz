from aiogram import Router, F, types
from aiogram.filters import Command
from db import queries
from pathlib import Path
from bot import bot

# from main import bot

car_router = Router()
queries.init_db()
img = Path('image')
list1 = []
for car in queries.get_marka():
    list1.append([types.InlineKeyboardButton(
        text=car[1], callback_data=f'marka {car[0]}'
    )])
kb = types.InlineKeyboardMarkup(inline_keyboard=list1)


@car_router.message(Command('cars'))
async def get(message: types.Message):
    # cars = queries.get_products()
    # for i in cars:
    #     file = types.FSInputFile(i[3])
    #     await message.answer_photo(photo=file, caption=(f'Марка: {i[1]} \n \n '
    #                                                     f'Цена: {i[2]}'))
    await message.answer('Выберите марку', reply_markup=kb)


@car_router.callback_query(F.data.startswith('marka '))
async def get_cars(call: types.CallbackQuery):
    id = call.data.replace('marka ', '')
    for car in queries.get_products(int(id)):
        file = types.FSInputFile(car[3])
        await bot.send_photo(chat_id=call.message.chat.id, photo=file, caption=(f'Марка: {car[1]} \n \n '
                                                                                f'Цена: {car[2]}'))