from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import buttons


@dp.message_handler(regexp=buttons.sent_btn, state=State.menu)
async def show_valentines(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('letters') == None:
        await message.answer(texts.no_sent, reply_markup=kb.menu_kb)
        return
    await message.answer(texts.outcomes, parse_mode="HTML", reply_markup=kb.menu_kb)
    for letter in data['letters']:
        await letter.send_copy(message.chat.id)

@dp.message_handler(regexp=buttons.send_btn, state=State.menu)
async def ask_for_receiver(message: types.Message):
    await message.answer(texts.for_whom, parse_mode="HTML")
    await State.wait_for_receiver.set()
