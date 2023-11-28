from aiogram import Router, types
from aiogram.filters import Command
from datetime import datetime
from db import queries

from bot import scheduler, bot

delayed_answer_router = Router()


# @delayed_answer_router.message(Command('remind'))
@delayed_answer_router.message()
async def remind():
    scheduler.add_job(
        send_remind,
        'date',
        run_date=datetime(2023, 11, 28, 18, 57, 0),
        # kwargs={'chat_id': message.from_user.id, }
    )
    # await message.answer('Напоминание установлено!')


async def send_remind():
    users = queries.receiving_user_id()
    for user in users:
        await bot.send_message(chat_id=user[0], text='Наступило 2024 год!')
