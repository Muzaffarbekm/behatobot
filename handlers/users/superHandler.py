from aiogram import types
from loader import dp

SUPERUSERS = ['172423241']

@dp.message_handler(chat_id=SUPERUSERS,text='secret')  # if chat id is superuser and if secret typed then go ahead
async def id_filter(message: types.Message):
    name = message.from_user.full_name
    await message.reply(f"Xush kelibsiz BOSS {name}")