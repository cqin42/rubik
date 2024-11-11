import sys
from moves import moveF

def init():
    return {
        "Top": [["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"]],
        "Bottom": [["🟨", "🟨", "🟨"], ["🟨", "🟨", "🟨"], ["🟨", "🟨", "🟨"]],
        "Left": [["🟩", "🟩", "🟩"], ["🟩", "🟩", "🟩"], ["🟩", "🟩", "🟩"]],
        "Right": [["🟦", "🟦", "🟦"], ["🟦", "🟦", "🟦"], ["🟦", "🟦", "🟦"]],
        "Front": [["🟥", "⬜", "🟥"], ["🟥", "🟥", "🟥"], ["🟥", "🟥", "🟥"]],
        "Back": [["🟧", "🟧", "🟧"], ["🟧", "🟧", "🟧"], ["🟧", "🟧", "🟧"]],
    }


def parsing(mv):
    lst = [
        "F",
        "R",
        "U",
        "B",
        "L",
        "D",
        "F’",
        "R’",
        "U’",
        "B’",
        "L’",
        "D’",
        "F2",
        "R2",
        "U2",
        "B2",
        "L2",
        "D2",
    ]
    for e in mv:
        assert e in lst, f"wrong moves {e}"


def main():
    assert len(sys.argv) == 2, "wrong number of arguments"
    move = sys.argv[1].split()
    parsing(move)
    rubik = init()
    moveF(rubik, "Front")
    print(rubik)


if __name__ == "__main__":
    main()