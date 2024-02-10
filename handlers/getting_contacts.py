from loader import dp, bot, ADMIN_IDS
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
from logic import edit_valentine
import buttons


@dp.message_handler(state=State.wait_for_receiver)
async def ask_for_sender(message: types.Message, state: FSMContext):
    await state.update_data(receiver=message.text)
    await message.answer(texts.for_sender, parse_mode="HTML", reply_markup=kb.anonim_kb)
    await State.wait_for_sender.set()


@dp.message_handler(state=State.wait_for_sender)
async def ask_for_letter(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(sender=message.text, backgroud=data.get('background'))
    edit_valentine(str(message.from_id) + '.png', data.get('background'), data.get('receiver'), message.text, data.get('text'), data.get('is_photo_set'), data.get('font'))
    with open('images/results/' + str(message.from_id) + '.png', 'rb') as f:
        await message.answer_photo(photo=f, caption=texts.letter_caption, parse_mode="HTML", reply_markup=kb.editing_menu_kb)
    await State.editing_letter_menu.set()

