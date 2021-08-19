from contextvars import Token
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.base import T
from wordChecker import checker
from local_settings import token

BOT_TOKEN = token

logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.reply("Behato botiga xush kelibsiz!")
    
@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply("Botni ishlatish uchun so'z yuboring")
    
    
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)