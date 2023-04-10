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
PLAYER1_SYMBOL = "X"
PLAYER2_SYMBOL = "O"


def get_players_symbol(player):
    if player == 1:
        return PLAYER1_SYMBOL
    if player == 2:
        return PLAYER2_SYMBOL
    return "-"


def draw_playground():
    playground = ""
    current_playfield = 0
    for row in range(COLUMN_COUNT):
        line = ""
        for field in range(COLUMN_COUNT):
            for selection_field in range(SELECTION_FIELD_WIDTH):
                if selection_field == calc_mid(SELECTION_FIELD_WIDTH):
                    line += get_players_symbol(
                        positions_status[current_playfield])
                    current_playfield += 1
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
    print(playground)
    print("\n")


def available_positions():
    positions = []
    for index, position in enumerate(positions_status):
        if position == 0:
            positions.append(index)
    return positions


def position_available(position_index):
    return position_index in available_positions()


def place_player_position(player, position):
    position_index = position - 1
    if not position_available(position_index):
        print(
            f"[PLAYER {1}]: Position {position} is not playable. Please choose an avaiable position!")
        print("\n")
        return
    positions_status[position_index] = player
    draw_playground()
    win_or_draw()


def win_or_draw():
    if positions_status[0] == 1 and positions_status[1] == 1 and positions_status[2] == 1:
        print("win")
        return True
    if positions_status[3] == 1 and positions_status[4] == 1 and positions_status[5] == 1:
        print("win")
        return True
    if positions_status[6] == 1 and positions_status[7] == 1 and positions_status[8] == 1:
        print("win")
        return True
    if positions_status[0] == 1 and positions_status[4] == 1 and positions_status[8] == 1:
        print("win")
        return True
    if positions_status[2] == 1 and positions_status[4] == 1 and positions_status[6] == 1:
        print("win")
        return True
    if positions_status[0] == 1 and positions_status[4] == 1 and positions_status[6] == 1:
        print("win")
        return True
    if positions_status[0] == 1 and positions_status[3] == 1 and positions_status[6] == 1:
        print("win")
        return True
    if positions_status[1] == 1 and positions_status[4] == 1 and positions_status[7] == 1:
        print("win")
        return True
    if positions_status[2] == 1 and positions_status[5] == 1 and positions_status[8] == 1:
        print("win")
        return True
    print("nothing")
    return False


draw_playground()
# place_player_position(1, 1)
# place_player_position(1, 2)
# place_player_position(1, 3)

# place_player_position(1, 4)
# place_player_position(1, 5)
# place_player_position(1, 6)

# place_player_position(1, 7)
# place_player_position(1, 8)
# place_player_position(1, 9)

# place_player_position(1, 1)
# place_player_position(1, 5)
# place_player_position(1, 9)

# place_player_position(1, 3)
# place_player_position(1, 5)
# place_player_position(1, 7)

# place_player_position(1, 1)
# place_player_position(1, 4)
# place_player_position(1, 7)

# place_player_position(1, 2)
# place_player_position(1, 5)
# place_player_position(1, 8)

# place_player_position(1, 3)
# place_player_position(1, 6)
# place_player_position(1, 9)

# p = input("PLAYER X [Symbol: Z]: Which Position would you take?\t")
