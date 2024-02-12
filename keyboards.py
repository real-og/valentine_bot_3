from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from buttons import *


menu_kb = ReplyKeyboardMarkup([[sent_btn, send_btn], [my_link_btn]],
                               resize_keyboard=True,
                               one_time_keyboard=True)

confirmation_kb = ReplyKeyboardMarkup([[change_btn,
                                         cancel_btn,],
                                        [confirm_btn]],
                                       resize_keyboard=True,
                                       one_time_keyboard=True)


editing_menu_kb = InlineKeyboardMarkup()
editing_menu_kb.add(InlineKeyboardButton(add_photo_btn, callback_data=add_photo_btn))
editing_menu_kb.insert(InlineKeyboardButton(change_backgroud_btn, callback_data=change_backgroud_btn))
editing_menu_kb.add(InlineKeyboardButton(add_text_btn, callback_data=add_text_btn))
editing_menu_kb.insert(InlineKeyboardButton(change_font_btn, callback_data=change_font_btn))
editing_menu_kb.add(InlineKeyboardButton(reset_btn, callback_data=reset_btn))
editing_menu_kb.add(InlineKeyboardButton(done_btn, callback_data=done_btn))


editing_back_kb = InlineKeyboardMarkup()
editing_back_kb.add(InlineKeyboardButton(prev_btn, callback_data=prev_btn))
editing_back_kb.insert(InlineKeyboardButton(choose_btn, callback_data=choose_btn))
editing_back_kb.insert(InlineKeyboardButton(next_btn, callback_data=next_btn))





