from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp

@dp.message_handler(Text(equals="salom",ignore_case=True))
@dp.message_handler(Text(contains="assalom",ignore_case=True))
@dp.message_handler(Text(startswith="assalom",ignore_case=True))
async def text_handler(message: types.Message):
    name = message.from_user.full_name
    await message.reply(f"Vaalaykum assalom {name} \n Tez orada siz bilan bog'lanamiz")


@dp.message_handler(Text(endswith=["rahmat","raxmat","salomat boling"],ignore_case=True))
async def welcome_me(message: types.Message):
    name = message.from_user.full_name
    await message.reply(f"Arzimaydi {name} ,so'rovingizni tezda ko'rib chiqamiz.")
    
@dp.message_handler(Text(endswith=["ahmoq","axmoq","jinni","jini","so'te","sotak"],ignore_case=True))
async def dont_swear(message: types.Message):
    name = message.from_user.full_name
    await message.reply(f"{name} bunday yomon gapirmang! Ban olib qolishingiz mumkin tez orada.")    