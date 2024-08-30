import random
import time

from data.c_key_positions import (pos_one, pos_two, pos_three, pos_four, pos_five,
                                  pos_six, pos_seven)
from utils.draw_fretboards import draw_terminal_fretboard

all_positions = {
    1: pos_one,
    2: pos_two,
    3: pos_three,
    4: pos_four,
    5: pos_five,
    6: pos_six,
    7: pos_seven
    }


def guess_position():
    print("\n\nYou will have 10 opportunities to guess position shapes\n\n")
    count = 1
    correct = 0
    incorrect = 0

    while count <= 10:
        pos_key = random.randint(1, 7)
        pos_val = all_positions[pos_key]
        illustration = draw_terminal_fretboard(pos_val)

        time.sleep(1)
        print(illustration)
        response = input("What position is this? (1-7)\n\n")

        try:
            response = int(response)

            if 1 <= response <= 7:
                if response == pos_key:
                    print("Correct! Well done!\n\n")
                    correct += 1
                else:
                    print("Incorrect. Try again.\n\n")
                    incorrect += 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.\n\n")

        count += 1

    print(f"You scored {correct/10*100} %")


guess_position()