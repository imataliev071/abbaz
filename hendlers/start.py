from aiogram import Router, F, types
from aiogram.filters import Command

stat_router = Router()


@stat_router.message(Command('start'))  # фильтр
async def start(message: types.Message):
    # await message.reply('hello')
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text='О нас', callback_data='about'
                ),
            ],
            [
                types.InlineKeyboardButton(
                    text='Наш канал', url='https://www.youtube.com/@MrBeast'
                ),
                types.InlineKeyboardButton(
                    text='Магазин', url='https://www.ebay.com/'
                )
            ]
        ]
    )
    await message.answer(f'Здравствуйте {message.from_user.first_name}',
                         reply_markup=kb,
                         )


@stat_router.callback_query(F.data == 'about')
async def about(clb: types.callback_query):
    await clb.message.answer('Хороший бот')
