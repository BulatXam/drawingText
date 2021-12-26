from pillow_draw_text import write_in_image


def main():
    text = "предложения разделить по словами пробелами и в каждую линию добавить по слову, пока не дойдет до лимита символов"
    draw_img = write_in_image(
        '../media/Jak_fresko.jpg',  # image for draw text
        text,                    # text
        xy=(100, 100),           # left and top
        width=600,               # width located text
        height=574)              # height located text
    draw_img.show()


if __name__ == '__main__':
    main()
