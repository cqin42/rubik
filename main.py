import sys
from moves import moveFront, moveTop, moveBottom, moveBack, moveFrontReverse, moveBackReverse, moveLeft, moveLeftReverse, moveRightReverse, moveBottomReverse, moveTopReverse

def print_rubik(cube):
    print("                " + " ".join(cube["Top"][0]))
    print("              " + " ".join(cube["Top"][1]))
    print("            " + " ".join(cube["Top"][2]))
    for i in range(3):
        print("  " + cube["Left"][i][0] + " " + cube["Left"][i][1] + " " + cube["Left"][i][2] + " " +
              cube["Front"][i][0] + " " + cube["Front"][i][1] + " " + cube["Front"][i][2] + " " +
              cube["Right"][i][0] + " " + cube["Right"][i][1] + " " + cube["Right"][i][2])
    print("            " + " ".join(cube["Bottom"][0]))
    print("              " + " ".join(cube["Bottom"][1]))
    print("                 " + " ".join(cube["Bottom"][2]))
    for i in range(2,-1,-1):
        print("            " + " " * 6 + cube["Back"][i][0] + " " + cube["Back"][i][1] + " " + cube["Back"][i][2])
    
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


def main():
    assert len(sys.argv) == 2, "wrong number of arguments"
    move = sys.argv[1].split()
    parsing(move)
    rubik = init()
    moveBottomReverse(rubik, "Bottom")
    print_rubik(rubik)
    for e in rubik:
        print(e, rubik[e])


if __name__ == "__main__":
    main()
