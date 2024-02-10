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

    draw.text((padding, padding), text_to, fill=(255, 255, 255), font=font)

    text2_bbox = draw.textbbox((0, 0), text_from, font=font)
    text2_position = (image.width - text2_bbox[2] - padding, image.height - text2_bbox[3] - padding)
    draw.text(text2_position, text_from, fill=(255, 255, 255), font=font)

    image.save('images/results/' + result_filename)

def add_photo(current_photo, file_to_add, output_image_path):
    size_expected = 600
    vertical_photo_padding = 110


    background_image = Image.open('images/results/' + current_photo)
    user_image = Image.open('images/buffer_files/' + file_to_add)

    user_width, user_height = user_image.size
    ratio = size_expected / max(user_width, user_height)
    user_image = user_image.resize((int(user_width * ratio), int(user_height * ratio)), Image.LANCZOS)


    bg_width, bg_height = background_image.size
    user_width, user_height = user_image.size

    x_offset = (bg_width - user_width) // 2
    y_offset = (bg_height - user_height) // 2

    background_image.paste(user_image, (x_offset, vertical_photo_padding))

    background_image.save('images/results/' + output_image_path)


def add_text(image_path, font_name, text, output_path):
    if len(text) > 150:
        return False
    max_len = 60
    if len(text) > max_len:
        split_index = len(text) // 2
        while text[split_index] != ' ':
            split_index -= 1
        text = text[:split_index] + '\n' + text[split_index+1:]

    image = Image.open('images/results/' + image_path)
    
    width, height = image.size
    
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.truetype("fonts/" + font_name, 50)
    
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = 710 + (900 - 710 - text_height) // 2
    
    draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)
    
    image.save('images/results/' + output_path)
    return True


