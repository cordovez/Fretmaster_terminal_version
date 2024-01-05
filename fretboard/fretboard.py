import random

from fretboard.seven_positions import (
    pos_five,
    pos_four,
    pos_one,
    pos_seven,
    pos_six,
    pos_three,
    pos_two,
)

POSTIONS = {
    1: pos_one,
    2: pos_two,
    3: pos_three,
    4: pos_four,
    5: pos_five,
    6: pos_six,
    7: pos_seven,
}


def draw_position(position):
    unfretted = "-------|"
    fretted = "-- ⏺ --|"
    fretboard = ""
    for array in position:
        string = "|"
        for binary in array:
            if binary == 0:
                string += unfretted
            else:
                string += fretted
        fretboard += string + "\n"
    print(fretboard)


def random_position():
    position_number = random.randint(1, 7)
    position_arrays = POSTIONS[position_number]
    random_fretboard = draw_position(position_arrays)
    return position_number
