from aiogram import types, Dispatcher
from aiogram.filters import Command

def register_handlers(dp: Dispatcher):

    @dp.message(Command("start"))
    async def start(message: types.Message):
        await message.answer("Привет 👋 Я карьерный бот. Нажми /menu, чтобы начать.")

    @dp.message(Command("menu"))
    async def menu(message: types.Message):
        keyboard = [
            [types.KeyboardButton(text="Обо мне и услугах")],
            [types.KeyboardButton(text="Записаться на консультацию")],
            [types.KeyboardButton(text="Материалы и чеклисты")],
        ]
        markup = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
        await message.answer("Выберите раздел:", reply_markup=markup)