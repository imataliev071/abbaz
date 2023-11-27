from aiogram import Router, F, types
from aiogram.filters import Command
from bot import bot
from db.queries import save_subscribe

stat_router = Router()


@stat_router.message(Command('start'))
async def start(message: types.Message):
    kb_start = types.InlineKeyboardMarkup(
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
                ),
            ],
            [
                types.InlineKeyboardButton(
                    text='Подписаться', callback_data='subscribe'
                )
            ]
        ]
    )
    await message.answer(
        f'Здравствуйте {message.from_user.first_name}',
        reply_markup=kb_start,
    )


@stat_router.callback_query(F.data.startswith('subscribe'))
async def get_cars(call: types.CallbackQuery):
    save_subscribe(call.message.chat.id)
    await bot.send_message(chat_id=call.message.chat.id, text="Вы подписаны")


@stat_router.callback_query(F.data == 'about')
async def about(clb: types.callback_query):
    await clb.message.answer('Хороший бот')
