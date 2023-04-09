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


# PLAYGROUND CONFIG #
COLUMN_COUNT = 3
SPACE_TO_SYMBOL = 2
SELECTION_FIELD_WIDTH = 5
PLAYGROUND_WIDTH = SELECTION_FIELD_WIDTH * COLUMN_COUNT + SPACE_TO_SYMBOL

# GAME SETUPS #
# these are the 9 posible positons to choose from
# 0 - open position
# 1 - player 1 field
# 2 - player 2 field
# only positions with status 0 can be edited
positions_status = [0, 0, 0, 0, 0, 0, 0, 0, 0]
avabilable_positions = []


def create_playground():
    playground = ""
    for row in range(COLUMN_COUNT):
        line = ""
        for field in range(COLUMN_COUNT):
            for selection_field in range(SELECTION_FIELD_WIDTH):
                if selection_field == calc_mid(SELECTION_FIELD_WIDTH):
                    line += "-"
                    continue
                line += " "
            if field != COLUMN_COUNT - 1:
                line += "|"
        playground += line + "\n"
        middle_line = ""
        if row != COLUMN_COUNT - 1:
            for x in range(PLAYGROUND_WIDTH):
                middle_line = middle_line + "-"
            playground += middle_line + "\n"
    return playground


def set_available_positions():
    for index, position in enumerate(positions_status):
        if position == 0:
            avabilable_positions.append(index)


def place_symbol(symbol, position):
    position_index = position - 1
    if position_index in avabilable_positions:
        positions_status[position_index] = symbol


print(create_playground())
set_available_positions()
print(place_symbol(1, 1))
print(place_symbol(2, 5))
print(positions_status)
# p = input("PLAYER X [Symbol: Z]: Which Position would you take?\t")
