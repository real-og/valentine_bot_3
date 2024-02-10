from PIL import Image, ImageDraw, ImageFont

def compose_letter(letter, receiver, sender):
    if letter.text:
        letter.text = f"От: {sender}\nКому: {receiver}\n{letter.text}"
    elif letter.caption:
        letter.caption = f"От: {sender}\nКому: {receiver}\n{letter.caption}"
    else:
        letter.caption = f"От: {sender}\nКому: {receiver}"
    return letter

def add_headers_to_background(backgroud_name, font_name, result_filename, receiver, sender):
    padding = 25

    image = Image.open("images/samples/" + backgroud_name)
    font = ImageFont.truetype("fonts/" + font_name, 60)
    draw = ImageDraw.Draw(image)

    text_to = 'Кому: ' + receiver
    text_from = 'От: ' + sender

    text1_bbox = draw.textbbox((0, 0), text_to, font=font)
    draw.text((padding, padding), text_to, fill=(255, 255, 255), font=font)

    text2_bbox = draw.textbbox((0, 0), text_from, font=font)
    text2_position = (image.width - text2_bbox[2] - padding, image.height - text2_bbox[3] - padding)
    draw.text(text2_position, text_from, fill=(255, 255, 255), font=font)

    image.save('images/results/' + result_filename)


