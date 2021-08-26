from aiogram import types
from loader import dp
from aiogram.dispatcher import filters

@dp.message_handler(is_reply=True,commands="user_id")
async def identify_id(message: types.Message):
    ids = message.from_user.id
    await message.reply(ids)
    
@dp.message_handler(content_types="contact",is_sender_contact=True)
async def contat_send(message: types.Message):
    await message.reply("Kontaktingiz qabul qilindi!")
    
@dp.message_handler(is_forwarded=True)
async def contat_send(message: types.Message):
    await message.reply("Forward qilish mumkin emas!")   
    
@dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE), commands="private") # if user writes /private go ahead
async def contat_send(message: types.Message):
    await message.reply("Siz shaxsiy habarlarga o'tdingiz!") 