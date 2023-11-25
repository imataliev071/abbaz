from aiogram import Router, F, types
from aiogram.filters import Command
from db import queries
from pathlib import Path
from bot import bot
from db.queries import save_bay_cars

# from main import bot

car_router = Router()
queries.init_db()
img = Path('image')
list1 = []
for car in queries.get_marka():
    list1.append([types.InlineKeyboardButton(
        text=car[1], callback_data=f'marka {car[0]}'
    )])
kb_marka = types.InlineKeyboardMarkup(inline_keyboard=list1)


@car_router.message(Command('cars'))
async def get(message: types.Message):
    # cars = queries.get_products()
    # for i in cars:
    #     file = types.FSInputFile(i[3])
    #     await message.answer_photo(photo=file, caption=(f'Марка: {i[1]} \n \n '
    #                                                     f'Цена: {i[2]}'))
    await message.answer('Выберите марку', reply_markup=kb_marka)


@car_router.callback_query(F.data.startswith('marka '))
async def get_cars(call: types.CallbackQuery):
    id = call.data.replace('marka ', '')
    for car in queries.get_products(int(id)):
        kb_buy = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text='Купить', callback_data=f"buy{car[0]}"
                    ),
                ]
            ]
        )
        file = types.FSInputFile(car[3])
        await bot.send_photo(reply_markup=kb_buy, chat_id=call.message.chat.id, photo=file,
                             caption=(f'Марка: {car[1]} \n \n '
                                      f'Цена: {car[2]}'))


@car_router.callback_query(F.data.startswith('buy'))
async def get_cars(call: types.CallbackQuery):
    id_car = int(call.data.replace('buy', ''))
    save_bay_cars(call.message.from_user.id, id_car)
    await bot.send_message(chat_id=call.message.chat.id, text="мы приняли ваш заказ")
