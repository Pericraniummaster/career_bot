from aiogram import types, Dispatcher

async def show_pricing(message: types.Message):
    text = (
        "💰 Прайс-лист на услуги:\n\n"
        "1️⃣ Аудит резюме — много\n"
        "2️⃣ Подготовка к собеседованию (1 час) — дохуя\n"
        "3️⃣ Пакет «Резюме + Подготовка к собеседованию» — дохуя и больше\n"
        "4️⃣ Консультация по карьерной стратегии — мальчик, потянешь?\n\n"
        "Для записи нажмите «Записаться на консультацию» 👇"
    )
    await message.answer(text)

def register_handlers(dp: Dispatcher):
    dp.message.register(show_pricing, lambda message: message.text == "Прайс-лист")
