from aiogram import types, Bot
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS, BOT_TOKEN
from keyboards.default.menu import menu_buttons
from keyboards.default.tanlov import menu_button
from loader import dp






bot = Bot(token=BOT_TOKEN)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    username = message.from_user.username
    fullname = message.from_user.full_name
    txt = "Admin botga xabar yubordi \n"
    txt += f"Username:@{username}\n"
    txt += f"Full name:{fullname}\n"
    txt+=f"id{message.from_user.id}\n"
    await bot.send_message(ADMINS[0],txt)
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_button)
