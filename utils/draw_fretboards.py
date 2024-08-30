from data.notes_on_fretboard import fretboard
import copy

def add_position(position: list) -> list[list[dict]]:
    """Function takes fretboard list and adds 'on' and 'root' keys and corresponding
    values"""
    fretboard_copy = copy.deepcopy(fretboard)
    for fret in fretboard_copy:
        for note in fret:
            if list(note.keys())[0] in position:
                note["on"] = True
            if "C" in list(note.values())[0]:
                note["root"] = True
    return fretboard_copy


def draw_terminal_fretboard(position: list) -> str:
    """This function is used to 'draw' the fretboard in the terminal to verify the shape
    of the position"""

    unfretted = "---|"
    fretted = "-⏺-|"
    draw = "=========================\n"
    fretboard_with_position = add_position(position)

    for fret in fretboard_with_position:
        string = "|"
        for note in fret:
            string += fretted if "on" in list(note.keys()) else unfretted
        draw += string + "\n"
    return draw


