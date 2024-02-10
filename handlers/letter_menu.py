from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
from buttons import *
import logic


@dp.callback_query_handler(state=State.editing_letter_menu)
async def pose_handler(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == done_btn:
        pass
    elif callback.data == add_photo_btn:
        pass
    elif callback.data == add_text_btn:
        pass
    elif callback.data == change_backgroud_btn:
        pass
    elif callback.data == change_font_btn:
        pass

    await callback.answer()