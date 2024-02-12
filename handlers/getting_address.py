from loader import dp, bot, ADMIN_IDS
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
from logic import edit_valentine, compose_letter
import buttons

@dp.message_handler(content_types=['text'], state=State.waiting_for_type)
async def ask_for_confirmation(message: types.Message, state: FSMContext): 
    await state.update_data(type=message.text)
    await State.waiting_for_address.set()
    await message.answer(texts.ask_for_address)


@dp.message_handler(content_types=['text'], state=State.waiting_for_address)
async def ask_for_confirmation(message: types.Message, state: FSMContext): 
    await state.update_data(address=message.text)
    data = await state.get_data()
    await State.menu.set()
    await message.answer(texts.back_to_menu, reply_markup=kb.menu_kb)
    for id in ADMIN_IDS:
        try:
            mes = await compose_letter(types.Message.to_object(data['letter']), data.get('address'), data.get('type'))
            await mes.send_copy(id)
        except Exception as e:
            print('error while broadcasting to admins')
            print(e)