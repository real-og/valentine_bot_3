from loader import dp, default_text, default_background,default_font, default_photo
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import json

def extract_unique_code(text):
    return text.split()[1] if len(text.split()) > 1 else None

@dp.message_handler(commands=['start'], state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    arg_code = extract_unique_code(message.text)
    if arg_code:
        await message.answer(texts.link_greeting)
        await state.update_data(text=default_text, font=default_font, background=default_background, is_photo_set=False, receiver_code=arg_code)
        await State.wait_for_receiver.set()
    else:
        await message.answer(texts.generate_greeting(message.from_user.id))
        await message.answer(texts.no_link_greeting, reply_markup=kb.menu_kb)
        await State.menu.set()


@dp.message_handler(commands=['help'], state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.help_message)
