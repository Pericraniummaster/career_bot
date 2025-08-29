from aiogram import types, Dispatcher

async def about_me(message: types.Message):
    text = (
        "👋 Привет! Я [Имя Фамилия]\n\n"
        "🎯 Помогаю с:\n"
        "- Разбором и улучшением резюме\n"
        "- Подготовкой к техническим и HR-собеседованиям\n"
        "- Навигацией по поиску работы в IT и смежных сферах\n\n"
        "📌 Мой опыт:\n"
        "- X лет в [сфера/отрасль]\n"
        "- Работал(а) в [компании]\n"
        "- Провёл(а) N+ консультаций\n\n"
        "Если хотите обсудить детали — жмите «Записаться на консультацию» 👇"
    )
    await message.answer(text)

def register_handlers(dp: Dispatcher):
    dp.message.register(about_me, lambda msg: msg.text == "Обо мне и услугах")