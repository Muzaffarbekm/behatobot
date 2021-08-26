from aiogram import types
from loader import dp

@dp.message_handler(commands="add_admin",is_chat_admin=True)
async def chat_admin_command(message: types.Message):
    await message.reply("BOSS kimmi admin qilish kere usernamelarini jo'nating!")
    
@dp.message_handler(commands="ban_user",is_chat_admin=True)
async def chat_admin_command(message: types.Message):
    await message.reply("BOSS kimmi ban qilish kerak usernamelarini jo'nating!")