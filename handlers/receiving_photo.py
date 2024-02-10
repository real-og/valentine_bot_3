from loader import dp, bot, ADMIN_IDS
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
from logic import compose_letter, add_headers_to_background, add_photo
import buttons

@dp.message_handler(content_types=['any'], state=State.wait_for_photo)
async def ask_for_confirmation(message: types.Message, state: FSMContext): 
    if message.content_type in ['photo']:
        await message.photo[-1].download(destination_file=f'images/buffer_files/{message.from_id}.jpg')
        add_photo(str(message.from_id) + '.png', str(message.from_id) + '.jpg', str(message.from_id) + '.png')
        with open('images/results/' + str(message.from_id) + '.png', 'rb') as f:
            await message.answer_photo(photo=f, caption=texts.letter_caption, parse_mode="HTML", reply_markup=kb.editing_menu_kb)
        await State.editing_letter_menu.set()
    else:
        await message.reply(texts.type_error)