from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    menu = State()
    wait_for_receiver = State()
    wait_for_sender = State()
    editing_letter_menu = State()
    wait_for_confirmation = State()
    wait_for_photo = State()
    wait_for_text = State()
    changing_background = State()
    changing_font = State()
    waiting_for_type = State()
    waiting_for_address = State()