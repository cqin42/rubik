import sys
from moves import moveFront, moveTop, moveBottom, moveBack, moveFrontReverse, moveBackReverse, moveLeft, moveLeftReverse, moveRightReverse, moveBottomReverse, moveTopReverse



def init():
    return {
        "Top": [["⬜", "⬜tt", "⬜"], ["⬜thomas", "⬜", "⬜"], ["⬜", "⬜", "atchoum⬜"]],
        "Bottom": [["🟨", "🟨paraplue", "🟨"], ["🟨aaaaaa", "🟨", "🟨"], ["🟨", "🟨", "🟨bbbb"]],
        "Left": [["yy", "🟩", "🟩"], ["🟩", "🟩", "🟩"], ["🟩", "🟩", "🟩"]],
        "Right": [["🟦", "🟦", "🟦"], ["🟦", "🟦", "🟦"], ["🟦", "🟦", "🟦"]],
        "Front": [["caca", "🟥", "🟥"], ["🟥", "🟥", "🟥"], ["🟥", "🟥", "🟥"]],
        "Back": [["hoho", "🟧ffff", "🟧"], ["🟧", "🟧", "roturier🟧"], ["🟧eee", "🟧", "🟧"]],
    }


def parsing(mv):
    lst = [
        "F",
        "R",
        "U",
        "B",
        "L",
        "D",
        "F'",
        "R'",
        "U'",
        "B'",
        "L'",
        "D'",
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
    moveBottomReverse(rubik, "Bottom")
    for e in rubik:
        print(e, rubik[e])


if __name__ == "__main__":
    main()
