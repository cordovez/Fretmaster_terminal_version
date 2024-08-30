from collections import namedtuple


Note = namedtuple('Note', ['index', 'note'])

positions_matrix = [
    # ["E0", "A0", "D0", "G0", "B0", "e0"], # Open strings
    # ==========================================
    ["E1", "A1", "D1", "G1", "B1", "e1"],
    ["E2", "A2", "D2", "G2", "B2", "e2"],
    ["E3", "A3", "D3", "G3", "B3", "e3"],
    # ——————————————————————————————————————————
    ["E4", "A4", "D4", "G4", "B4", "e4"],
    ["E5", "A5", "D5", "G5", "B5", "e5"],
    # ——————————————————————————————————————————
    ["E6", "A6", "D6", "G6", "B6", "e6"],
    ["E7", "A7", "D7", "G7", "B7", "e7"],
    # ——————————————————————————————————————————
    ["E8", "A8", "D8", "G8", "B8", "e8"],
    ["E9", "A9", "D9", "G9", "B9", "e9"],
    # ——————————————————————————————————————————
    ["E10", "A10", "D10", "G10", "B10", "e10"],
    ["E11", "A11", "D11", "G11", "B11", "e11"],
    # ——————————————————————————————————————————
    ["E12", "A12", "D12", "G12", "B12", "e12"],
    ["E13", "A13", "D13", "G13", "B13", "e13"],
    ["E14", "A14", "D14", "G14", "B14", "e14"],
    ["E15", "A15", "D15", "G15", "B15", "e15"]
    # ——————————————————————————————————————————
    ]

notes_positions = [
    {'index': 'e1', 'note': 'F'},
    {'index': 'e2', 'note': 'Gb'},
    {'index': 'e3', 'note': 'G'},
    {'index': 'e4', 'note': 'Ab'},
    {'index': 'e5', 'note': 'A'},
    {'index': 'e6', 'note': 'Bb'},
    {'index': 'e7', 'note': 'B'},
    {'index': 'e8', 'note': 'C'},
    {'index': 'e9', 'note': 'Db'},
    {'index': 'e10', 'note': 'D'},
    {'index': 'e11', 'note': 'Eb'},
    {'index': 'e12', 'note': 'E'},
    {'index': 'B1', 'note': 'C'},
    {'index': 'B2', 'note': 'Db'},
    {'index': 'B3', 'note': 'D'},
    {'index': 'B4', 'note': 'Eb'},
    {'index': 'B5', 'note': 'E'},
    {'index': 'B6', 'note': 'F'},
    {'index': 'B7', 'note': 'Gb'},
    {'index': 'B8', 'note': 'G'},
    {'index': 'B9', 'note': 'Ab'},
    {'index': 'B10', 'note': 'A'},
    {'index': 'B11', 'note': 'Bb'},
    {'index': 'B12', 'note': 'B'},
    {'index': 'G1', 'note': 'Ab'},
    {'index': 'G2', 'note': 'A'},
    {'index': 'G3', 'note': 'Bb'},
    {'index': 'G4', 'note': 'B'},
    {'index': 'G5', 'note': 'C'},
    {'index': 'G6', 'note': 'Db'},
    {'index': 'G7', 'note': 'D'},
    {'index': 'G8', 'note': 'Eb'},
    {'index': 'G9', 'note': 'E'},
    {'index': 'G10', 'note': 'F'},
    {'index': 'G11', 'note': 'Gb'},
    {'index': 'G12', 'note': 'G'},
    {'index': 'D1', 'note': 'Eb'},
    {'index': 'D2', 'note': 'E'},
    {'index': 'D3', 'note': 'F'},
    {'index': 'D4', 'note': 'Gb'},
    {'index': 'D5', 'note': 'G'},
    {'index': 'D6', 'note': 'Ab'},
    {'index': 'D7', 'note': 'A'},
    {'index': 'D8', 'note': 'Bb'},
    {'index': 'D9', 'note': 'B'},
    {'index': 'D10', 'note': 'C'},
    {'index': 'D11', 'note': 'Db'},
    {'index': 'D12', 'note': 'D'},
    {'index': 'A1', 'note': 'Bb'},
    {'index': 'A2', 'note': 'B'},
    {'index': 'A3', 'note': 'C'},
    {'index': 'A4', 'note': 'Db'},
    {'index': 'A5', 'note': 'D'},
    {'index': 'A6', 'note': 'Eb'},
    {'index': 'A7', 'note': 'E'},
    {'index': 'A8', 'note': 'F'},
    {'index': 'A9', 'note': 'Gb'},
    {'index': 'A10', 'note': 'G'},
    {'index': 'A11', 'note': 'Ab'},
    {'index': 'A12', 'note': 'A'},
    {'index': 'E1', 'note': 'F'},
    {'index': 'E2', 'note': 'Gb'},
    {'index': 'E3', 'note': 'G'},
    {'index': 'E4', 'note': 'Ab'},
    {'index': 'E5', 'note': 'A'},
    {'index': 'E6', 'note': 'Bb'},
    {'index': 'E7', 'note': 'B'},
    {'index': 'E8', 'note': 'C'},
    {'index': 'E9', 'note': 'Db'},
    {'index': 'E10', 'note': 'D'},
    {'index': 'E11', 'note': 'Eb'},
    {'index': 'E12', 'note': 'E'}]


def find_note_value(position: str) -> str:
    """Given the position passed, find the note value among notes_positions"""
    for item in notes_positions:
        if position == item['index']:
            return item['note']


def create_fretboard_matrix(matrix: list[list]) -> list[list]:
    """Given the shape of the matrix passed in, create a new matrix with notes and
    positions as named tuples"""
    fretboard = []
    for fret in matrix:
        fret_group = []
        for i in fret:
            match_note = find_note_value(i)
            note = Note(i, match_note)
            fret_group.append({str(i): match_note})
            # fret_group.append({str(i): note})

        fretboard.append(fret_group)
    return fretboard


final_matrix = create_fretboard_matrix(positions_matrix)
print(final_matrix)
