from aiogram import Router, types
from aiogram.filters import Command
from random import choice
from pathlib import Path

picture_router = Router()

list = []

img = Path('image')
for i in img.iterdir():
    list.append(i)


@picture_router.message(Command('picture'))  # фильтр
async def pic(message: types.Message):
    file = types.FSInputFile(choice(list))
    await message.answer_photo(photo=file)
    print(file)
