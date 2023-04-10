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


def switch_players(player):
    if player == 1:
        return 2
    return 1


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
    for index, pos in enumerate(positions_status):
        if pos == 0:
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


def win_or_draw(player):
    win_message = f"WINNN for PLAYER {player}"
    for i in range(3):
        if all(positions_status[i*3 + j] == player for j in range(3)):
            print(win_message)
            return True
        if all(positions_status[j*3 + i] == player for j in range(3)):
            print(win_message)
            return True
    if all(positions_status[i*3 + i] == player for i in range(3)):
        print(win_message)
        return True
    if all(positions_status[i*3 + (2-i)] == player for i in range(3)):
        print(win_message)
        return True
    if all_positions_used():
        print("DRAWW")
        return True
    return False


def all_positions_used():
    return positions_status.count(0) <= 0


draw_playground()
current_player = 1
while not win_or_draw(current_player):
    position = input(
        f"PLAYER {current_player}: Which Position would you take?\n" +
        f"Available positions: {[pos + 1 for pos in available_positions()]}\n" +
        "=> ")
    print("\n")
    place_player_position(current_player, int(position))
    if win_or_draw(current_player):
        break
    current_player = switch_players(current_player)

# p = input("PLAYER X [Symbol: Z]: Which Position would you take?\t")
