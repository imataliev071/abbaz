from aiogram import Router, types
from aiogram.filters import Command
from datetime import datetime

from bot import scheduler, bot

delayed_answer_router = Router()


@delayed_answer_router.message(Command('remind'))
async def remind(message: types.Message):
    scheduler.add_job(
        send_remind,
        'date',
        run_date=datetime(2023, 12, 31,23,59,59),
        kwargs={'chat_id': message.from_user.id, }
    )
    await message.answer('Напоминание установлено!')


async def send_remind(chat_id: int):
    await bot.send_message(chat_id=chat_id, text='Наступило 2024 год!')



