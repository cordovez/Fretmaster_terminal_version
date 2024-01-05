ALL_NOTES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
STRINGS = ["e", "B", "G", "D", "A", "E"]
FRETBOARD = range(0, 13)
FRETS = []


def create_fretboard():
    fret_id = 1
    for string in STRINGS:
        for position in FRETBOARD:
            if position != 0:
                FRETS.append(
                    {
                        "string": string,
                        "fret": position,
                        "index": fret_id,
                        "note": None,
                    }
                )
                fret_id += 1


def add_note_value() -> None:
    for fret in FRETS:
        string = fret["string"].upper()

        string_index = ALL_NOTES.index(string)

        new_position = (string_index + fret["fret"]) % len(ALL_NOTES)

        fret["note"] = ALL_NOTES[new_position]


def notes_on_12_frets():
    create_fretboard()
    add_note_value()

    return FRETS
