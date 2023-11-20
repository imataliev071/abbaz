from aiogram.types import BotCommand
import asyncio
from aiogram import Bot, Dispatcher, types
import logging
from dotenv import load_dotenv
from os import getenv
from hendlers import (
    stat_router,
    echo_router,
    myinfo_ruter,
    picture_router,
    shop_router,
    questions_router,
    car_router
)
from db.queries import init_db, create_tables, populate_tables


async def on_startup(dispatcher):
    init_db()
    create_tables()
    populate_tables()


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


async def main():
    await bot.set_my_commands([
        BotCommand(command='start', description='Старт'),
        BotCommand(command='picture', description='Случайная кртинка'),
        BotCommand(command='myinfo', description='Информация об о мне'),
        BotCommand(command='shop', description='Магазин'),
        BotCommand(command='quest', description='Опрос'),
        BotCommand(command='get', description='машины')
    ])
    dp.include_router(car_router)
    dp.include_router(questions_router)
    dp.include_router(stat_router)
    dp.include_router(shop_router)
    dp.include_router(myinfo_ruter)
    dp.include_router(picture_router)
    dp.startup.register(on_startup)
    dp.include_router(echo_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
