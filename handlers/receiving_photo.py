from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
from logic import edit_valentine


@dp.message_handler(content_types=['any'], state=State.wait_for_photo)
async def ask_for_confirmation(message: types.Message, state: FSMContext): 
    
    if message.content_type in ['photo']:
        await state.update_data(is_photo_set=True)
        data = await state.get_data()
        await message.photo[-1].download(destination_file=f'images/buffer_files/{message.from_id}.png')
        await edit_valentine(str(message.from_id) + '.png', data.get('background'), data.get('receiver'), data.get('sender'), data.get('text'), data.get('is_photo_set'), data.get('font'))
        with open('images/results/' + str(message.from_id) + '.png', 'rb') as f:
            await message.answer_photo(photo=f, caption=texts.letter_caption, parse_mode="HTML", reply_markup=kb.editing_menu_kb)
        await State.editing_letter_menu.set()
        await state.update_data(is_photo_set=True)
    else:
        await message.reply(texts.type_error)