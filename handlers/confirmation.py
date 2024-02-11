from loader import dp, ADMIN_IDS
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import buttons

@dp.message_handler(regexp=buttons.confirm_btn, state=State.wait_for_confirmation)
async def confirm_letter(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('letters') == None:
        data['letters'] = []
    data['letters'].append(data['letter'])
    for id in ADMIN_IDS:
        try:
            mes = types.Message.to_object(data['letter'])
            await mes.send_copy(id)
        except Exception as e:
            print('**1**')
            print(e)
    await state.update_data(letters=data['letters'])
    await message.answer(texts.after_confirmed, parse_mode="HTML", reply_markup=kb.menu_kb)
    await State.menu.set()

@dp.message_handler(regexp=buttons.change_btn, state=State.wait_for_confirmation)
async def change_letter(message: types.Message, state: FSMContext):
    await message.answer(texts.after_changed, parse_mode="HTML")
    with open('images/results/' + str(message.from_id) + '.png', 'rb') as f:
        await message.answer_photo(photo=f, caption=texts.letter_caption, parse_mode="HTML", reply_markup=kb.editing_menu_kb)
    await State.editing_letter_menu.set()

@dp.message_handler(regexp=buttons.cancel_btn, state=State.wait_for_confirmation)
async def cancel_letter(message: types.Message, state: FSMContext):
    await message.answer(texts.after_canceled, parse_mode="HTML", reply_markup=kb.menu_kb)
    await State.menu.set()