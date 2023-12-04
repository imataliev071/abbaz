from aiogram.types import BotCommand
import asyncio
import logging
from hendlers.delayed_answer import remind
from hendlers import (
    stat_router,
    echo_router,
    myinfo_ruter,
    picture_router,
    shop_router,
    questions_router,
    car_router,
    group_messages_router
)
from db.queries import init_db, create_tables, populate_tables
from bot import bot, dp, scheduler


async def on_startup(dispatcher):
    init_db()
    create_tables()
    populate_tables()
    await remind()


async def main():
    await bot.set_my_commands([
        BotCommand(command='start', description='Старт'),
        BotCommand(command='picture', description='Случайная картинка'),
        BotCommand(command='myinfo', description='Информация об о мне'),
        BotCommand(command='shop', description='Магазин'),
        BotCommand(command='questions', description='Опрос'),
        BotCommand(command='cars', description='Цены на машины'),
    ])
    dp.include_router(car_router)
    dp.include_router(questions_router)
    dp.include_router(stat_router)
    dp.include_router(shop_router)
    dp.include_router(myinfo_ruter)
    dp.include_router(picture_router)
    dp.include_router(group_messages_router)

    dp.startup.register(on_startup)

    dp.include_router(echo_router)
    # запуск планировщика
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
