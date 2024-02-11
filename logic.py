from PIL import Image, ImageDraw, ImageFont
import os

def compose_letter(letter, receiver, sender):
    if letter.text:
        letter.text = f"От: {sender}\nКому: {receiver}\n{letter.text}"
    elif letter.caption:
        letter.caption = f"От: {sender}\nКому: {receiver}\n{letter.caption}"
    else:
        letter.caption = f"От: {sender}\nКому: {receiver}"
    return letter


def get_next_back(current_back, shift):
    files = sorted(os.listdir('images/samples'))
    index = files.index(current_back)
    index += shift
    if index == len(files):
        return files[0]
    return files[index]


def get_next_font(current_font, shift):
    files = sorted(os.listdir('fonts'))
    index = files.index(current_font)
    index += shift
    if index == len(files):
        return files[0]
    return files[index]

async def edit_valentine(original, back, receiver, sender, text, is_photo_set, font_name):
    padding = 25
    caption_size = 47
    font_size = 63
    font_color = (255, 255, 255)

    if font_name == 'vasek.ttf':
        caption_size = int(caption_size * 1.3)
        font_size = int(font_size * 1.3)

    if back in ['color3.png', 'color8.png', 'color9.png']:
        font_color = (20, 20, 20)

    image = Image.open("images/samples/" + back)
    font = ImageFont.truetype("fonts/" + font_name, caption_size)
    draw = ImageDraw.Draw(image)

    text_to = 'Кому: ' + receiver
    text_from = 'От: ' + sender

    draw.text((padding, padding), text_to, fill=font_color, font=font)

    text2_bbox = draw.textbbox((0, 0), text_from, font=font)
    text2_position = (image.width - text2_bbox[2] - padding, image.height - text2_bbox[3] - padding)
    draw.text(text2_position, text_from, fill=font_color, font=font)

    if is_photo_set:
        size_expected = 600
        vertical_photo_padding = 120
        
        user_image = Image.open('images/buffer_files/' + original)

        user_width, user_height = user_image.size
        ratio = size_expected / max(user_width, user_height)
        user_image = user_image.resize((int(user_width * ratio), int(user_height * ratio)), Image.LANCZOS)


        bg_width, bg_height = image.size
        user_width, user_height = user_image.size

        x_offset = (bg_width - user_width) // 2
        y_offset = (bg_height - user_height) // 2

        image.paste(user_image, (x_offset, vertical_photo_padding))

    if len(text) > 150:
        return False
    max_len = 60
    if len(text) > max_len:
        split_index = len(text) // 2
        while text[split_index] != ' ':
            split_index -= 1
        text = text[:split_index] + '\n' + text[split_index+1:]

    width, height = image.size
    
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.truetype("fonts/" + font_name, font_size)
    
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = 710 + (900 - 710 - text_height) // 2
    
    draw.text((text_x, text_y), text, fill=font_color, font=font)
    
    image.save('images/results/' + original)
    return True

