from aiogram import types
from loader import dp


@dp.message_handler(is_reply=True,commands="user_id")
async def identify_id(message: types.Message):
    ids = message.from_user.id
    await message.reply(ids)