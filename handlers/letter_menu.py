from loader import dp, default_text, default_background,default_font, default_photo
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
        await state.update_data(letter=letter.to_python())
        await callback.message.answer(texts.for_confirmation, parse_mode="HTML", reply_markup=kb.confirmation_kb)
        await State.wait_for_confirmation.set()
    if callback.data == reset_btn:
        await callback.message.delete()
        await callback.message.answer(texts.for_whom)
        await state.update_data(text=default_text, font=default_font, background=default_background, is_photo_set=False)
        await State.wait_for_receiver.set()
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
        letter = await callback.message.edit_caption(caption=texts.choose_font, reply_markup=kb.editing_back_kb)
        await State.changing_font.set()

    await callback.answer()