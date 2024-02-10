from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from buttons import *


menu_kb = ReplyKeyboardMarkup([['Отправленные📁', 'Отправить💌']],
                               resize_keyboard=True,
                               one_time_keyboard=True)

confirmation_kb = ReplyKeyboardMarkup([['Изменить🔁',
                                         'Отменить❌',],
                                        ['Подтвердить✅']],
                                       resize_keyboard=True,
                                       one_time_keyboard=True)

anonim_kb = ReplyKeyboardMarkup([['Аноним']],
                               resize_keyboard=True,
                               one_time_keyboard=True)

editing_menu_kb = InlineKeyboardMarkup()
editing_menu_kb.add(InlineKeyboardButton(add_photo_btn, callback_data=add_photo_btn))
editing_menu_kb.insert(InlineKeyboardButton(change_backgroud_btn, callback_data=change_backgroud_btn))
editing_menu_kb.add(InlineKeyboardButton(add_text_btn, callback_data=add_text_btn))
editing_menu_kb.insert(InlineKeyboardButton(change_font_btn, callback_data=change_font_btn))
editing_menu_kb.add(InlineKeyboardButton(done_btn, callback_data=done_btn))