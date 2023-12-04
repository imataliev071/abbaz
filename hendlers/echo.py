from aiogram import Router, types

echo_router = Router()


@echo_router.message()  # декоратор
async def echo(message: types.Message):  # обрабодчик
    print(message.chat.type)
    await message.reply(message.text)  # ответ тем же с показом вопроса
    # await message.answer('hi') #ответ
    # await message.answer(message.text)  # ответ сообщением
    # print(message)
    # print(message.text)
