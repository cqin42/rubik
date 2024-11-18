import numpy as np

# lst = [
#         "F", ok moveFront
#         "R", ok moveRight
#         "U", ok moveTopBottom
#         "B", ok moveBack
#         "L", ok moveLeft
#         "D", ok moveTopBottom

#         "F’",moveFrontReverse
#         "R’",moveRighttReverse
#         "U’",
#         "B’",moveBackReverse
#         "L’",moveLeftReverse
#         "D’",

#         "F2",
#         "R2",
#         "U2",
#         "B2",
#         "L2",
#         "D2",
#     ]


def moveFront(rubik, direction):
    fb = 2
    rubik[direction] = np.rot90(rubik[direction], 3)
    lastTopLine = rubik["Top"][fb]
    firstColumnRight = [rubik["Right"][i][0] for i in range(3)]
    lastBottomLine = rubik["Bottom"][fb]
    lastColumnLeft = [rubik["Left"][i][fb] for i in range(3)]

    rubik["Top"][fb] = lastColumnLeft
    for i in range (3):
        rubik["Right"][i][0] = lastTopLine[i]
    rubik["Bottom"][fb] = firstColumnRight
    for i in range (3):
        rubik["Left"][i][2] = lastBottomLine[i]

def moveBack(rubik, direction):
    fb = 0
    rubik[direction] = np.rot90(rubik[direction], 3)
    lastTopLine = rubik["Top"][fb]
    firstColumnRight = [rubik["Right"][i][0] for i in range(3)]
    lastBottomLine = rubik["Bottom"][fb]
    lastColumnLeft = [rubik["Left"][i][fb] for i in range(3)]

    rubik["Top"][fb] = firstColumnRight
    for i in range (3):
        rubik["Right"][i][2] = lastBottomLine[i]
    rubik["Bottom"][fb] = lastColumnLeft
    for i in range (3):
        rubik["Left"][i][0] = lastTopLine[i]

def moveBottom(rubik, direction):
    ud = 0 if direction == "Top" else 2
    rubik[direction] = np.rot90(rubik[direction], 3 if ud == 0 else 1)

    firstRowBack = rubik["Back"][ud]
    firstRowLeft = rubik["Left"][ud]
    firstRowFront = rubik["Front"][ud]
    firstRowRight = rubik["Right"][ud]

    rubik["Back"][ud] = firstRowRight
    rubik["Left"][ud] = firstRowBack
    rubik["Front"][ud] = firstRowLeft
    rubik["Right"][ud] = firstRowFront

def moveTop(rubik, direction):
    ud = 0 if direction == "Top" else 2
    rubik[direction] = np.rot90(rubik[direction], 3 if ud == 0 else 1)

    firstRowBack = rubik["Back"][ud]
    firstRowLeft = rubik["Left"][ud]
    firstRowFront = rubik["Front"][ud]
    firstRowRight = rubik["Right"][ud]

    rubik["Back"][ud] = firstRowLeft
    rubik["Left"][ud] = firstRowFront
    rubik["Front"][ud] = firstRowRight
    rubik["Right"][ud] = firstRowBack

def moveRight(rubik, side):
    rl = 2
    lastColumnFront = [rubik["Front"][i][rl] for i in range(3)]
    lastColumnTop = [rubik["Top"][i][rl] for i in range(3)]
    lastColumnBack = [rubik["Back"][i][0 if rl == 2 else 2] for i in range(3)]
    lastColumnBottom = [rubik["Bottom"][i][rl] for i in range(3)]

    for i in range(3):
        rubik["Front"][i][rl] = lastColumnBottom[i]
    for i in range(3):
        rubik["Top"][i][rl] = lastColumnFront[i]
    for i in range(3):
        rubik["Back"][i][0 if rl == 2 else 2] = lastColumnTop[i]
    for i in range(3):
        rubik["Bottom"][i][rl] = lastColumnBack[i]

    rubik[side] = np.rot90(rubik[side], 1)

def moveLeft(rubik, side):
    rl = 0
    lastColumnFront = [rubik["Front"][i][rl] for i in range(3)]
    lastColumnTop = [rubik["Top"][i][rl] for i in range(3)]
    lastColumnBack = [rubik["Back"][i][0 if rl == 2 else 2] for i in range(3)]
    lastColumnBottom = [rubik["Bottom"][i][rl] for i in range(3)]

    for i in range(3):
        rubik["Front"][i][rl] = lastColumnTop[i]
    for i in range(3):
        rubik["Top"][i][rl] = lastColumnBack[i]
    for i in range(3):
        rubik["Back"][i][0 if rl == 2 else 2] = lastColumnBottom[i]
    for i in range(3):
        rubik["Bottom"][i][rl] = lastColumnFront[i]

    rubik[side] = np.rot90(rubik[side], 3)

def moveFrontReverse(rubik, direction):
    fb = 2
    rubik[direction] = np.rot90(rubik[direction], 1)
    lastTopLine = rubik["Top"][fb]
    firstColumnRight = [rubik["Right"][i][0] for i in range(3)]
    lastBottomLine = rubik["Bottom"][fb]
    lastColumnLeft = [rubik["Left"][i][fb] for i in range(3)]

    rubik["Top"][fb] = firstColumnRight
    for i in range (3):
        rubik["Right"][i][0 if fb == 2 else 2] = lastBottomLine[i]
    rubik["Bottom"][fb] = lastColumnLeft
    for i in range (3):
        rubik["Left"][i][2 if fb == 2 else 0] = lastTopLine[i]


def moveBackReverse(rubik, direction):
    fb = 0
    rubik[direction] = np.rot90(rubik[direction], 1)
    lastTopLine = rubik["Top"][fb]
    firstColumnRight = [rubik["Right"][i][0] for i in range(3)]
    lastBottomLine = rubik["Bottom"][fb]
    lastColumnLeft = [rubik["Left"][i][fb] for i in range(3)]

    rubik["Top"][fb] = lastColumnLeft
    for i in range (3):
        rubik["Right"][i][2] = lastTopLine[i]
    rubik["Bottom"][fb] = firstColumnRight
    for i in range (3):
        rubik["Left"][i][0] = lastBottomLine[i]

def moveLeftReverse(rubik, side):
    rl = 0
    lastColumnFront = [rubik["Front"][i][rl] for i in range(3)]
    lastColumnTop = [rubik["Top"][i][rl] for i in range(3)]
    lastColumnBack = [rubik["Back"][i][2] for i in range(3)]
    lastColumnBottom = [rubik["Bottom"][i][rl] for i in range(3)]

    for i in range(3):
        rubik["Front"][i][rl] = lastColumnBottom[i]
    for i in range(3):
        rubik["Top"][i][rl] = lastColumnFront[i]
    for i in range(3):
        rubik["Back"][i][2] = lastColumnTop[i]
    for i in range(3):
        rubik["Bottom"][i][rl] = lastColumnBack[i]

    rubik[side] = np.rot90(rubik[side], 1)


def moveRightReverse(rubik, side):
    rl = 2
    lastColumnFront = [rubik["Front"][i][rl] for i in range(3)]
    lastColumnTop = [rubik["Top"][i][rl] for i in range(3)]
    lastColumnBack = [rubik["Back"][i][0] for i in range(2,-1,-1)]
    lastColumnBottom = [rubik["Bottom"][i][rl] for i in range(3)]

    for i in range(3):
        rubik["Front"][i][rl] = lastColumnTop[i]
    for i in range(3):
        rubik["Top"][i][rl] = lastColumnBack[i]
    for i in range(3):
        rubik["Back"][i][0 if rl == 2 else 2] = lastColumnBottom[i]
    for i in range(3):
        rubik["Bottom"][i][rl] = lastColumnFront[i]

    rubik[side] = np.rot90(rubik[side], 3)


def moveTopReverse(rubik, direction):
    ud = 0 if direction == "Top" else 2
    rubik[direction] = np.rot90(rubik[direction], 1 if ud == 0 else 3)

    firstRowBack = rubik["Back"][ud]
    firstRowLeft = rubik["Left"][ud]
    firstRowFront = rubik["Front"][ud]
    firstRowRight = rubik["Right"][ud]

    rubik["Back"][ud] = firstRowRight
    rubik["Left"][ud] = firstRowBack
    rubik["Front"][ud] = firstRowLeft
    rubik["Right"][ud] = firstRowFront

def moveBottomReverse(rubik, direction):
    ud = 0 if direction == "Top" else 2
    rubik[direction] = np.rot90(rubik[direction], 3)

    firstRowBack = rubik["Back"][ud]
    firstRowLeft = rubik["Left"][ud]
    firstRowFront = rubik["Front"][ud]
    firstRowRight = rubik["Right"][ud]

    rubik["Back"][ud] = firstRowLeft
    rubik["Left"][ud] = firstRowFront
    rubik["Front"][ud] = firstRowRight
    rubik["Right"][ud] = firstRowBack
