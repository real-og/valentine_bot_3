from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


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