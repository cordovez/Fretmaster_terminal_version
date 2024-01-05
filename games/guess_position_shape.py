from fretboard.fretboard import random_position


def guess_position():
    print("\n\nYou will have 10 opportunities to guess position shapes\n\n")
    count = 0
    correct = 0
    incorrect = 1
    while count <= 10:
        position = random_position()
        response = input("What position is this? (1-7)\n\n")

        if response.isdigit() and 1 <= int(response) <= 7:
            # Check if the user's input is correct
            if int(response) == position:
                print("Correct! Well done!\n\n")
                correct += 1
                # break  # Exit the loop if the input is correct
            else:
                print("Incorrect. Try again.\n\n")
                incorrect += 1

        else:
            print("Invalid input. Please enter a number between 1 and 7.")
        count += 1
    print(f"You scored {correct} correct and {incorrect} incorrect\n\n")
