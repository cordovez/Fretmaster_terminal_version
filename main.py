import pprint
from data.c_key_positions import (pos_one, pos_two, pos_three, pos_four, pos_five,
                                  pos_six, pos_seven)
from utils.draw_fretboards import draw_terminal_fretboard
from games.guess_position_shape import guess_position
pp = pprint.PrettyPrinter(indent=2)


def main():
    # print( draw_terminal_fretboard(pos_one))
    guess_position()


if __name__ == "__main__":
    main()
