from loader import dp, ADMIN_IDS
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import buttons
from logic import compose_letter

@dp.message_handler(regexp=buttons.confirm_btn, state=State.wait_for_confirmation)
async def confirm_letter(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('letters') == None:
        data['letters'] = []
    data['letters'].append(data['letter'])
    receiver_id = data.get('receiver_code')

    # sending to target
    try:
        mes = types.Message.to_object(data['letter'])
        await mes.send_copy(receiver_id)
        await message.answer(texts.success_sending)
    except:
        await message.answer(texts.error_sending)


    # resending to admins during testing
    for id in ADMIN_IDS:
        try:
            captioned_mess = await compose_letter(types.Message.to_object(data['letter']), str(receiver_id), message.from_id)
            await captioned_mess.send_copy(id)
        except Exception as e:
            print('**1**')
            print(e)


    await state.update_data(letters=data['letters'], receiver_code=message.from_user.id)
    await message.answer(texts.menu_message, reply_markup=kb.menu_kb)
    await State.menu.set()


@dp.message_handler(regexp=buttons.change_btn, state=State.wait_for_confirmation)
async def change_letter(message: types.Message, state: FSMContext):
    await message.answer(texts.after_changed)
    with open('images/results/' + str(message.from_id) + '.png', 'rb') as f:
        await message.answer_photo(photo=f, caption=texts.letter_caption, reply_markup=kb.editing_menu_kb)
    await State.editing_letter_menu.set()

@dp.message_handler(regexp=buttons.cancel_btn, state=State.wait_for_confirmation)
async def cancel_letter(message: types.Message, state: FSMContext):
    await message.answer(texts.after_canceled)
    await message.answer(texts.menu_message, reply_markup=kb.menu_kb)
    await State.menu.set()

@dp.message_handler(state=State.wait_for_confirmation)
async def ask_for_receiver(message: types.Message, state: FSMContext):
    await message.answer(texts.use_buttons, reply_markup=kb.confirmation_kb)