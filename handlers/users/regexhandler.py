from aiogram import types
from aiogram.dispatcher.filters import Regexp,RegexpCommandsFilter
from loader import dp


EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_REGEX = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
IP = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}'
START_WITH_EMAIL = r"email:" + EMAIL_REGEX

@dp.message_handler(Regexp(EMAIL_REGEX))
async def email(message: types.Message):
    name = message.from_user.full_name
    await message.reply(f"{name} emailingiz qabul qilindi, tez orada javob yozamiz!")

@dp.message_handler(Regexp(PHONE_REGEX))
async def email(message: types.Message):
    name = message.from_user.full_name
    await message.reply(f"{name} telefon raqamingiz qabul qilindi, tez orada operator aloqaga chiqadi!")
    
@dp.message_handler(regexp_commands=[IP])
async def start_with_email(message: types.Message):
    name = message.from_user.full_name
    await message.reply(f"emailingiz qabul bo'ldi, tez orada javob yozamiz!")
    
