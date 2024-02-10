from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
from buttons import *


@dp.callback_query_handler(state=State.editing_letter_menu)
async def pose_handler(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == done_btn:
        letter = await callback.message.edit_caption(caption='')
        await state.update_data(letter=letter)
        await callback.message.answer(texts.for_confirmation, parse_mode="HTML", reply_markup=kb.confirmation_kb)
        await State.wait_for_confirmation.set()
    elif callback.data == add_photo_btn:
        letter = await callback.message.edit_caption(caption='')
        await callback.message.answer(texts.send_photo)
        await State.wait_for_photo.set()
    elif callback.data == add_text_btn:
        letter = await callback.message.edit_caption(caption='')
        await callback.message.answer(texts.send_text)
        await State.wait_for_text.set()
    elif callback.data == change_backgroud_btn:
        letter = await callback.message.edit_caption(caption=texts.choose_background, reply_markup=kb.editing_back_kb)
        await State.changing_background.set()
    elif callback.data == change_font_btn:
        pass

    await callback.answer()