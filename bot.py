import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import start, form  # импортируем хэндлеры

# Загружаем токен
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Логирование
logging.basicConfig(level=logging.INFO)

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Регистрируем хэндлеры
start.register_handlers(dp)
form.register_handlers(dp)

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())