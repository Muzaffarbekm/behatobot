from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply("Botni ishlatish uchun so'z yuboring")
    
