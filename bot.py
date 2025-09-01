import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import start, form, about, pricing, materials  # importing handlers

# Loading token
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Logging
logging.basicConfig(level=logging.INFO)

# Bot and Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Handlers registration
start.register_handlers(dp)
form.register_handlers(dp)
about.register_handlers(dp)
pricing.register_handlers(dp)
materials.register_handlers(dp)

# Run long-polling
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())