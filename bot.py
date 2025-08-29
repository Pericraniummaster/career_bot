import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv

# Loading token from .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Logging
logging.basicConfig(level=logging.INFO)

# Creating bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Handling /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет 👋 Я карьерный бот. Нажми /menu, чтобы начать.")

# Handling /menu
@dp.message(Command("menu"))
async def menu(message: types.Message):
    keyboard = [
        [types.KeyboardButton(text="Обо мне и услугах")],
        [types.KeyboardButton(text="Записаться на консультацию")],
        [types.KeyboardButton(text="Материалы и чеклисты")],
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await message.answer("Выберите раздел:", reply_markup=markup)

# Running the bot
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
