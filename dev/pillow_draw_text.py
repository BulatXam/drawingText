from PIL import Image, ImageDraw, ImageFont


def split_lines(text, line_size):
    """Функция для разреза текста на строки.

    Выводит список со строками символов,
    которые не больше требуемого максимума. """
    split_text = text.split(" ")
    lines = []
    line = ""
    word_count = 0

    for _ in split_text:
        line += split_text[word_count]+" "

        if len(line) > line_size:
            lines.append(line)
            line = ""

        word_count += 1

        # Останавливаем цикл, когда доходим до последнего слова
        if word_count+1 == len(split_text):
            line += split_text[word_count] + " "
            lines.append(line)
            break

    return lines


def split_text_into_lines(text, width, font_size):
    """Фунция для разреза текста с помощью символа новой строки-\n
    
    Соединяет список из строк в цельный текст"""
    letters_count_in_line = int(width / (font_size/2))
    split_lines_text = \
        "\n".join(split_lines(text, line_size=letters_count_in_line))

    return split_lines_text


def write_in_image(image_path: str,
                   text: str,
                   xy: list,
                   width: int,
                   height: int,
                   font_size: int = 50,
                   font: ImageFont or None = None) -> Image:
    image = Image.open(image_path)

    if not font:
        font = ImageFont.truetype(
            "../media/sans-serif.ttf",
            size=font_size
        )

    split_text = split_text_into_lines(
        text=text,
        width=width,
        height=height,
        font_size=font_size,
    )

    draw_text = ImageDraw.Draw(image)
    draw_text.text(
        xy=xy,
        text=split_text,
        font=font,
        fill='#1C0606'
    )

    return image
