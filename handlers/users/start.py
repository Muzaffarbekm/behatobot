import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from contextvars import Token
from aiogram import Bot, Dispatcher, executor, types
from wordChecker import checker
from data.config import ADMINS,BOT_TOKEN 
from aiogram.dispatcher.filters.state import State, StatesGroup

BOT_TOKEN = BOT_TOKEN

logging.basicConfig(level=logging.INFO)


class Form(StatesGroup):
    search = State()
    

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
    
@dp.message_handler(commands='search')
async def checkSpelling(message: types.Message,state=FSMContext):
    await Form.search.set()

    word = message.text
    result = checker(word)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
    await message.answer(response)       
 
@dp.message_handler(state=Form.search)
async def checkSpelling(message: types.Message,state=FSMContext): 
    await message.reply("Qidirgan so'zingiz bo'yicha javoblar yuqorida berildi")
    await state.finish()
    
    
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
