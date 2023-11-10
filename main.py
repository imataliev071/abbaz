# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
from dotenv import load_dotenv
from os import getenv

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


@dp.message(Command('start'))  # фильтр
async def start(message: types.Message):
    # await message.reply('hello')
    await message.answer(f'Здравствуйте {message.from_user.first_name}')


@dp.message(Command('myinfo'))  # фильтр
async def myinfo(message: types.Message):
    await message.answer(
        f'Ваш id: {message.from_user.id} \nВаше имя: {message.from_user.first_name} \nВаш user name: {message.from_user.username}')


@dp.message(Command('picture'))  # фильтр
async def picture(message: types.Message):
    file = types.FSInputFile('image/wallpaperbetter.com_3840x2160.jpg')
    await message.answer_photo(photo=file)


@dp.message()  # декоратор
async def echo(message: types.Message):  # обрабодчик
    # await message.reply(message.text)  # ответ тем же с показом вопроса
    # await message.answer('hi') #ответ
    await message.answer(message.text)  # ответ сообщением
    # print(message)
    # print(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
