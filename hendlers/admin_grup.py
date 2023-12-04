from aiogram import Router, F, types
from aiogram.filters import Command
from bot import bot
from pprint import pprint

group_messages_router = Router()
BAD_WORDS = ('fff', 'g')


# @group_messages_router.message(F.from_user.id == 123456789)
# @group_messages_router.message((F.from_user.id == 123456789) | (F.from_user.id == 3213123123))
# @group_messages_router.message(F.from_user.id.in_({123456789, 3213123123}))
# @group_messages_router.message((F.chat.type == "group") & (F.from_user.id == 123456789))
# @group_messages_router.message(F.chat.type.in_({"group", "supergroup"}))
@group_messages_router.message(Command("ban", prefix="!/"))
async def ban_user(message: types.Message):
    reply = message.reply_to_message
    if reply is not None:
        await message.bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=reply.from_user.id
        )
        await message.answer(f"Пользователь {message.from_user.first_name} забанен")


@group_messages_router.message(Command("pin", prefix="!/"))
async def pin_message(message: types.Message):
    reply = message.reply_to_message
    if reply is not None:
        await message.bot.pin_chat_message(
            chat_id=message.chat.id,
            message_id=reply.message_id
        )


@group_messages_router.message(F.chat.type == "supergroup")
async def catch_bad_words(message: types.Message):
    # print(message.chat.type)
    for word in BAD_WORDS:
        if word in message.text.lower():
            await message.reply(f"Нельзя использовать слово {word}!")
            await message.delete()
            # await bot.kick_chat_member(message.chat.id, message.from_user.id)
            await bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id
                )
            await message.answer(f"Пользователь {message.from_user.first_name} забанен")

            break
