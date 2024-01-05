import pprint

from games.guess_position_shape import guess_position
from scales.music_notes import notes_on_12_frets

pp = pprint.PrettyPrinter(indent=4)


#
all_notes = notes_on_12_frets()


def main():
    response = input(
        "\n\nPick your choice:\n\n A) Print note values for every fret \n B) Play a game of 10 guesses for position shapes\n\n"
    )
    print(response)
    if response.upper() == "A":
        pp.pprint(all_notes)
    else:
        guess_position()


if __name__ == "__main__":
    main()
