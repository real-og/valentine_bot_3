greeting = """<b>Привет!</b>\n
Здесь ты можешь написать своё послание, а мы доставим его в осязаемом виде.\n
<i>Нажимай Отправить, чтобы начать</i>"""

outcomes = "Валентинки <b>от тебя:</b>"

for_whom = """<b>Кому:</b>
Напиши, кому доставить"""

for_sender = """Как тебя подписать? (От кого)
<i>Не обязательно писать своё имя, анонимность допускается</i>"""

for_letter = "Наконец-то время <b>заветного послания:</b>🙃"

for_confirmation = """Это твоя валентинка
Если всё хорошо - <b>Подтвердить</b>
Чтобы заполнить заново - <b>Изменить</b>"""

after_confirmed = "<b>Подтверждено</b>"

after_changed = """Семь раз отмерь, один раз отрежь.
Заполняй снова"""

after_canceled = "Отравка отменена"
default = "Используй кнопки или /start чтобы начать заново"

no_sent = 'Нет отправленных'

letter_caption = 'Это твоя валентинка'

send_photo = 'Присылай фото'
send_text = 'Присылай текст'

type_error = 'Мне нужно именно фото'

too_long_text = 'Слишком длинный текст'

choose_background = 'Выбирай фон нажимая на кнопки'
choose_font= 'Выбирай шрифт'

help_message = '/start - чтобы начать заново'

ask_for_type = 'Выберите, как доставить письмо. В бумажном конверте или онлайн.'

ask_for_address = """Введите контакты адресата:

ФИО / Е-mail/ Ник в Телеграм для электронного варианта.

ФИО и физический адрес для бумажного варианта."""

back_to_menu = "Готово! Открытка будет доставлена получателю администратором.\nТы в меню"

link_greeting = """<b>Привет!</b> Ты перешел по ссылке, давай отправим валентинку!

Как подпишем получателя? Проще говоря - <b>КОМУ:</b>"""


def generate_greeting(id):
    return f"""<b>Привет!</b> Ты перешел НЕ по ссылке. Чтобы люди могли отправлять тебе анонимные послания, размести эту ссылку у себя в соц.сетях ⬇️

t.me/try_and_take_bot?start={id}

Тот, кто перейдет, сможет писать тебе анонимные валентинки"""

no_link_greeting = 'Пока можешь попробовать, как выглядит создание валентинки (кнопка <b>Попробовать💌</b>) \nОна отправится тебе же.'