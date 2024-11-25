import sys
from moves import (
    moveFront,
    moveTop,
    moveBottom,
    moveBack,
    moveFrontReverse,
    moveBackReverse,
    moveLeft,
    moveLeftReverse,
    moveRightReverse,
    moveBottomReverse,
    moveTopReverse,
    moveRight,
)
from firstLayerEdges import firstLayerEdge


def print_rubik(cube):
    for i in range(2, -1, -1):
        keys = []
        for j in range(3):
            keys += [k for k, v in cube["Top"][i][j].items()]
        print("            " + " ".join(keys), end="\n")
    left_keys, front_keys, right_keys, back_keys, bottom_keys = (
        [],
        [],
        [],
        [],
        [],
    )
    for i in range(3):
        for j in range(3):
            left_keys += [k for k, v in cube["Left"][i][j].items()]
            front_keys += [k for k, v in cube["Front"][i][j].items()]
            right_keys += [k for k, v in cube["Right"][i][j].items()]
            back_keys += [k for k, v in cube["Back"][i][j].items()]
            bottom_keys += [k for k, v in cube["Bottom"][i][j].items()]

    tmp, str = 3, ""
    ll = [left_keys, front_keys, right_keys, back_keys]
    for i in range(3):
        for e in ll:
            tmp -= 3
            str += " " if e != left_keys else ""
            for j in range(3):
                str += e[tmp] + " "
                tmp += 1
            tmp += 3 if e == back_keys else 0
        str += "\n"
    tmp = 0
    for i in range(3):
        str += "            "
        for j in range(3):
            str += bottom_keys[tmp] + " "
            tmp += 1
        str += "\n"
    print(str)


def init():
    return {
        "Top": [
            [{"⬜": [1, 1, 1]}, {"⬜": [2, 2, 1]}, {"⬜": [3, 1, 2]}],
            [{"⬜": [4, 2, 2]}, {"⬜": [5, 0, 0]}, {"⬜": [6, 2, 3]}],
            [{"⬜": [7, 1, 3]}, {"⬜": [8, 2, 4]}, {"⬜": [9, 1, 4]}],
        ],
        "Front": [
            [{"🟥": [10, 1, 1]}, {"🟥": [11, 2, 1]}, {"🟥": [12, 1, 2]}],
            [{"🟥": [13, 2, 2]}, {"🟥": [14, 0, 0]}, {"🟥": [15, 2, 3]}],
            [{"🟥": [16, 1, 3]}, {"🟥": [17, 2, 4]}, {"🟥": [18, 1, 4]}],
        ],
        "Right": [
            [{"🟦": [19, 1, 1]}, {"🟦": [20, 2, 1]}, {"🟦": [21, 1, 2]}],
            [{"🟦": [22, 2, 2]}, {"🟦": [23, 0, 0]}, {"🟦": [24, 2, 3]}],
            [{"🟦": [25, 1, 3]}, {"🟦": [26, 2, 4]}, {"🟦": [27, 1, 4]}],
        ],
        "Back": [
            [{"🟧": [28, 1, 1]}, {"🟧": [29, 2, 1]}, {"🟧": [30, 1, 2]}],
            [{"🟧": [31, 2, 2]}, {"🟧": [32, 0, 0]}, {"🟧": [33, 2, 3]}],
            [{"🟧": [34, 1, 3]}, {"🟧": [35, 2, 4]}, {"🟧": [36, 1, 4]}],
        ],
        "Left": [
            [{"🟩": [37, 1, 1]}, {"🟩": [38, 2, 1]}, {"🟩": [39, 1, 2]}],
            [{"🟩": [40, 2, 2]}, {"🟩": [41, 0, 0]}, {"🟩": [42, 2, 3]}],
            [{"🟩": [43, 1, 3]}, {"🟩": [44, 2, 4]}, {"🟩": [45, 1, 4]}],
        ],
        "Bottom": [
            [{"🟨": [46, 1, 1]}, {"🟨": [47, 2, 1]}, {"🟨": [48, 1, 2]}],
            [{"🟨": [49, 2, 2]}, {"🟨": [50, 0, 0]}, {"🟨": [51, 2, 3]}],
            [{"🟨": [52, 1, 3]}, {"🟨": [53, 2, 4]}, {"🟨": [54, 1, 4]}],
        ],
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
    d = {
        "F": ["Front", moveFront],
        "R": ["Right", moveRight],
        "U": ["Top", moveTop],
        "B": ["Back", moveBack],
        "L": ["Left", moveLeft],
        "D": ["Bottom", moveBottom],
        "F'": ["Front", moveFrontReverse],
        "R'": ["Right", moveRightReverse],
        "U'": ["Top", moveTopReverse],
        "B'": ["Back", moveBackReverse],
        "L'": ["Left", moveLeftReverse],
        "D'": ["Bottom", moveBottomReverse],
    }
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
    print("-----------------------------------------")
    firstLayerEdge(rubik)


if __name__ == "__main__":
    main()
