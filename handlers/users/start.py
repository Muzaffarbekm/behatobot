import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from contextvars import Token
from aiogram import Bot, Dispatcher, executor, types
from wordChecker import checker
from data.config import ADMINS,BOT_TOKEN 

BOT_TOKEN = BOT_TOKEN

logging.basicConfig(level=logging.INFO)


# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)

@dp.message_handler(CommandStart(deep_link='hello'))
async def welcome(message: types.Message):
    info = message.get_args()
    text = f"Assalomu alaykum {message.from_user.full_name}!\n Siz {info} orqali qoshildizngiz!"   
    await message.reply(text)
    
   
@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    info = message.get_args()
    text = f"Assalomu alaykum {message.from_user.full_name}!\nBehato botiga xush kelibsiz"   
    await message.reply(text)
    
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo_handler(message: types.Message):
    info = message.get_args()
    text = f"Xurmatli {message.from_user.full_name}!\n Buni nimaligiga aniqlik kiritsak?"   
    await message.reply(text)    
    
@dp.message_handler()
async def checkSpelling(message: types.Message):
    word = message.text
    result = checker(word)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
    await message.answer(response)       
    
    
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
