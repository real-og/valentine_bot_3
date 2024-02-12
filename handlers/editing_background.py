from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import keyboards as kb
from states import State
from buttons import *
from logic import edit_valentine, get_next_back


@dp.callback_query_handler(state=State.changing_background)
async def pose_handler(callback: types.CallbackQuery, state: FSMContext):
    if callback.data in [next_btn, prev_btn]:
        data = await state.get_data()
        if callback.data == next_btn:
            shift = 1
        else:
            shift = -1
        new_back = get_next_back(data.get('background'), shift)
        await state.update_data(background=new_back)
        await edit_valentine(str(callback.message.chat.id) + '.png', new_back, data.get('receiver'), data.get('sender'), data.get('text'), data.get('is_photo_set'), data.get('font'))
        with open('images/results/' + str(callback.message.chat.id) + '.png', 'rb') as f:
            await callback.message.edit_media(types.InputMediaPhoto(media=f), reply_markup=kb.editing_back_kb)

    elif callback.data == choose_btn:
        await callback.message.edit_caption(caption='', reply_markup=kb.editing_menu_kb)
        await State.editing_letter_menu.set()

    await callback.answer()