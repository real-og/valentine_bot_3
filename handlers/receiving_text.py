from loader import dp, bot, ADMIN_IDS
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
from logic import compose_letter, add_headers_to_background, add_photo, add_text
import buttons

@dp.message_handler(content_types=['text'], state=State.wait_for_text)
async def ask_for_confirmation(message: types.Message, state: FSMContext): 
    data = await state.get_data()
    if add_text(str(message.from_id) + '.png', data.get('font'), message.text, str(message.from_id) + '.png'):
        with open('images/results/' + str(message.from_id) + '.png', 'rb') as f:
            await message.answer_photo(photo=f, caption=texts.letter_caption, parse_mode="HTML", reply_markup=kb.editing_menu_kb)
        await State.editing_letter_menu.set()
    else:
        await message.answer(texts.too_long_text)
    
