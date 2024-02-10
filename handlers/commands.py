from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb

@dp.message_handler(commands=['start'], state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.greeting, parse_mode="HTML", reply_markup=kb.menu_kb)
    await State.menu.set()