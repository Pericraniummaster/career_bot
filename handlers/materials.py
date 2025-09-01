from aiogram import types, Dispatcher
from aiogram.types import InputFile
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_DIR = os.path.join(BASE_DIR, "files")  # files/  folder with materials

async def send_materials(message: types.Message):
    # Send all files from the files/ directory
    files = os.listdir(FILES_DIR)
    if not files:
        await message.answer("Материалы пока не загружены.")
        return

    for filename in files:
        path = os.path.join(FILES_DIR, filename)
        doc = InputFile(path)
        await message.answer_document(doc, caption=filename)

def register_handlers(dp: Dispatcher):
    dp.message.register(send_materials, lambda msg: msg.text == "Материалы и чеклисты")
