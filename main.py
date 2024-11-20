import sys
from moves import moveFront, moveTop, moveBottom, moveBack, moveFrontReverse, moveBackReverse, moveLeft, moveLeftReverse, moveRightReverse, moveBottomReverse, moveTopReverse, moveRight

def print_rubik(cube):
    for i in range(3):
        print("            " + " ".join(cube["Top"][i]))
    for i in range(3):
        print("  " + cube["Left"][i][0] + " " + cube["Left"][i][1] + " " + cube["Left"][i][2] + " " +
              cube["Front"][i][0] + " " + cube["Front"][i][1] + " " + cube["Front"][i][2] + " " +
              cube["Right"][i][0] + " " + cube["Right"][i][1] + " " + cube["Right"][i][2])
    for i in range(3):
        print("            " + " ".join(cube["Bottom"][i]))
    for i in range(2,-1,-1):
        print("       " + " " * 6 + cube["Back"][i][0] + " " + cube["Back"][i][1] + " " + cube["Back"][i][2])

def init():
    return {
        "Top": [["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"], ["⬜", "⬜", "⬜"]],
        "Bottom": [["🟨", "🟨", "🟨"], ["🟨", "🟨", "🟨"], ["🟨", "🟨", "🟨"]],
        "Left": [["🟩", "🟩", "🟩"], ["🟩", "🟩", "🟩"], ["🟩", "🟩", "🟩"]],
        "Right": [["🟦", "🟦", "🟦"], ["🟦", "🟦", "🟦"], ["🟦", "🟦", "🟦"]],
        "Front": [["🟥", "🟥", "🟥"], ["🟥", "🟥", "🟥"], ["🟥", "🟥", "🟥"]],
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

def moveRubik(move, rubik):
    d = {"F": ["Front", moveFront],
        "R": ["Right", moveRight],
        "U": ["Top", moveTop],
        "B": ["Back", moveBack],
        "L":["Left", moveLeft],
        "D":["Bottom", moveBottom],
        "F'": ["Front", moveFrontReverse],
        "R'": ["Right", moveRightReverse],
        "U'": ["Top", moveTopReverse],
        "B'": ["Back", moveBackReverse],
        "L'":["Left", moveLeftReverse],
        "D'":["Bottom", moveBottomReverse],}
    for e in move:
        if e in d:
            d[e][1](rubik, d[e][0])
        elif "2" in e:
            for i in range(2):
                d[e.replace("2", "")][1](rubik, d[e.replace("2", "")][0])

def main():
    assert len(sys.argv) == 2, "wrong number of arguments"
    move = sys.argv[1].split()
    parsing(move)
    rubik = init()
    moveRubik(move, rubik)
    for e in rubik:
        print(e, rubik[e])
    print_rubik(rubik)


if __name__ == "__main__":
    main()
