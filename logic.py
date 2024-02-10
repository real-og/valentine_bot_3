def compose_letter(letter, receiver, sender):
    if letter.text:
        letter.text = f"От: {sender}\nКому: {receiver}\n{letter.text}"
    elif letter.caption:
        letter.caption = f"От: {sender}\nКому: {receiver}\n{letter.caption}"
    else:
        letter.caption = f"От: {sender}\nКому: {receiver}"
    return letter

