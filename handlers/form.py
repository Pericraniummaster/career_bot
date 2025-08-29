from aiogram import types, Dispatcher, Bot
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

# --- Состояния анкеты ---
class Form(StatesGroup):
    goal = State()
    service = State()
    format = State()
    time = State()

def register_handlers(dp: Dispatcher):

    @dp.message(lambda msg: msg.text == "Записаться на консультацию")
    async def cmd_start_form(message: types.Message, state: FSMContext):
        await message.answer("Отлично 👍 Давайте начнём!\n\nКакая у вас цель?", 
                             reply_markup=ReplyKeyboardRemove())
        await state.set_state(Form.goal)

    @dp.message(Form.goal)
    async def process_goal(message: types.Message, state: FSMContext):
        await state.update_data(goal=message.text)
        await message.answer("Какая услуга интересует? (Аудит резюме / Подготовка к интервью / Консультация / Пакет)")
        await state.set_state(Form.service)

    @dp.message(Form.service)
    async def process_service(message: types.Message, state: FSMContext):
        await state.update_data(service=message.text)
        await message.answer("Какой формат удобен? (Звонок / Письменный разбор)")
        await state.set_state(Form.format)

    @dp.message(Form.format)
    async def process_format(message: types.Message, state: FSMContext):
        await state.update_data(format=message.text)
        await message.answer("Когда вам удобно? (Напишите дату/время или примерный диапазон)")
        await state.set_state(Form.time)

    @dp.message(Form.time)
    async def process_time(message: types.Message, state: FSMContext, bot: Bot):
        await state.update_data(time=message.text)

        data = await state.get_data()
        result = (
            f"📩 Новая заявка!\n\n"
            f"🎯 Цель: {data['goal']}\n"
            f"🛠 Услуга: {data['service']}\n"
            f"📞 Формат: {data['format']}\n"
            f"⏰ Время: {data['time']}\n"
            f"👤 От: @{message.from_user.username or message.from_user.id}"
        )

        # Отправка тебе (замени chat_id на свой ID)
        YOUR_CHAT_ID = 308978895
        await bot.send_message(YOUR_CHAT_ID, result)

        await message.answer("Спасибо 🙌 Ваша заявка отправлена! Я свяжусь с вами в ближайшее время.")
        await state.clear()