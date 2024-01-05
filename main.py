import pprint

from fretboard.fretboard import random_position

pp = pprint.PrettyPrinter(indent=4)


def main():
    print(random_position())
    # pp.pprint(notes_on_12_frets())


if __name__ == "__main__":
    main()
