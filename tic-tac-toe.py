import os
from time import sleep


def clear_console(): return os.system("clear")

# t = input("WElches feld? =")

# text = ""
# for x in range(100):
#     print(text)
#     text += "| "
#     sleep(0.8)
#     clear_console()


def calc_mid(number):
    return round(number / 2)


def add_new_line(string):
    return string + "\n"


# playground config
COLUMN_COUNT = 3
SPACE_TO_SYMBOL = 2
SELECTION_FIELD_WIDTH = 5
PLAYGROUND_WIDTH = SELECTION_FIELD_WIDTH * COLUMN_COUNT + SPACE_TO_SYMBOL


def draw_playground_line():
    line = ""
    for field in range(COLUMN_COUNT):
        for selection_field in range(SELECTION_FIELD_WIDTH):
            if selection_field == calc_mid(SELECTION_FIELD_WIDTH):
                line = line + "-"
                continue
            line = line + " "
        if field != COLUMN_COUNT - 1:
            line = line + "|"
    line = add_new_line(line)
    for x in range(PLAYGROUND_WIDTH):
        line = line + "-"
    line = add_new_line(line)
    print(line)


draw_playground_line()
