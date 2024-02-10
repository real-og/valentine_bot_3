from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    menu = State()
    wait_for_receiver = State()
    wait_for_letter = State()
    wait_for_sender = State()
    wait_for_confirmation = State()