from aiogram import Router, F, types
from aiogram.filters import Command

shop_router = Router()


@shop_router.message(Command('shop'))
async def shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Дизайнер'),
                types.KeyboardButton(text='В начало', url='https://www.youtube.com/@MrBeast'),
            ],
            [
                types.KeyboardButton(text='Программирования')
            ]
        ],
        resize_keyboard=True
    )
    await message.answer('Выберите категория', reply_markup=kb)


@shop_router.message(F.text == 'Дизайнер')
async def diziner(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('-Дизайнер моделирование\n-Дизайнер интерьера', reply_markup=kb)


@shop_router.message(F.text == 'Программирования')
async def arhitettor(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('Front-end разработка\nBack-end разработка', reply_markup=kb)


@shop_router.message(F.text == 'В начало')
async def start(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer('/start', reply_markup=kb)
