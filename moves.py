

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


def rotate(n):
    buf = {}
    t = 0
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                buf[t] = n[i][j]
                t += 1
    li = [5, 3, 0, 6, 1, 7, 4, 2]
    tmp = 0
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                n[i][j] = buf[li[tmp]]
                tmp += 1


def rotateReverse(n):
    buf = {}
    t = 0
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                buf[t] = n[i][j]
                t += 1
    li = [2, 4, 7, 1, 6, 0, 3, 5]
    tmp = 0
    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                n[i][j] = buf[li[tmp]]
                tmp += 1


def moveFront(rubik, direction):
    rotate(rubik["Front"])
    lastTopLine = rubik["Top"][0]
    firstColumnRight = [rubik["Right"][i][0] for i in range(3)]
    lastBottomLine = rubik["Bottom"][0]
    lastColumnLeft = [rubik["Left"][i][2] for i in range(3)]

    rubik["Top"][0] = lastColumnLeft
    for i in range(3):
        rubik["Right"][i][0] = lastTopLine[i]
    rubik["Bottom"][0] = firstColumnRight
    for i in range(3):
        rubik["Left"][i][2] = lastBottomLine[i]


def moveBack(rubik, direction):
    rotate(rubik["Back"])
    lastTopLine = rubik["Top"][2]
    firstColumnRight = [rubik["Right"][i][2] for i in range(3)]
    lastBottomLine = rubik["Bottom"][2]
    lastColumnLeft = [rubik["Left"][i][0] for i in range(3)]

    rubik["Top"][2] = firstColumnRight
    tmp = 0
    for i in range(2,-1,-1):
        rubik["Right"][tmp][2] = lastBottomLine[i]
        tmp += 1
    rubik["Bottom"][2] = lastColumnLeft
    tmp = 0
    for i in range(2,-1,-1):
        rubik["Left"][tmp][0] = lastTopLine[i]
        tmp += 1


def moveBottom(rubik, direction):
    ud = 2

    rotate(rubik["Bottom"])
    firstRowBack = rubik["Back"][ud]
    firstRowLeft = rubik["Left"][ud]
    firstRowFront = rubik["Front"][ud]
    firstRowRight = rubik["Right"][ud]

    rubik["Back"][ud] = firstRowRight
    rubik["Left"][ud] = firstRowBack
    rubik["Front"][ud] = firstRowLeft
    rubik["Right"][ud] = firstRowFront


def moveTop(rubik, direction):
    ud = 0
    rotateReverse(rubik["Top"])

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
    tmp = 0
    for i in range(2,-1,-1):
        rubik["Top"][tmp][rl] = lastColumnFront[i]
        tmp +=1
    for i in range(3):
        rubik["Back"][i][0 if rl == 2 else 2] = lastColumnTop[i]
    tmp = 0
    for i in range(2,-1,-1):
        rubik["Bottom"][tmp][rl] = lastColumnBack[i]
        tmp += 1

    rotate(rubik["Right"])


def moveLeft(rubik, side):
    rl = 0
    lastColumnFront = [rubik["Front"][i][rl] for i in range(3)]
    lastColumnTop = [rubik["Top"][i][rl] for i in range(3)]
    lastColumnBack = [rubik["Back"][i][0 if rl == 2 else 2] for i in range(3)]
    lastColumnBottom = [rubik["Bottom"][i][rl] for i in range(3)]

    tmp = 0
    for i in range(2,-1,-1):
        rubik["Front"][tmp][rl] = lastColumnTop[i]
        tmp += 1
    for i in range(3):
        rubik["Top"][i][rl] = lastColumnBack[i]
    tmp = 0
    for i in range(2,-1,-1):
        rubik["Back"][tmp][0 if rl == 2 else 2] = lastColumnBottom[i]
        tmp += 1
    for i in range(3):
        rubik["Bottom"][i][rl] = lastColumnFront[i]

    rotate(rubik["Left"])


def moveFrontReverse(rubik, direction):
    rotateReverse(rubik["Front"])
    lastTopLine = rubik["Top"][0]
    firstColumnRight = [rubik["Right"][i][0] for i in range(3)]
    lastBottomLine = rubik["Bottom"][0]
    lastColumnLeft = [rubik["Left"][i][2] for i in range(3)]

    rubik["Top"][0] = firstColumnRight
    for i in range(3):
        rubik["Right"][i][0] = lastBottomLine[i]
    rubik["Bottom"][0] = lastColumnLeft
    for i in range(3):
        rubik["Left"][i][2] = lastTopLine[i]


def moveBackReverse(rubik, direction):
    rotateReverse(rubik["Back"])
    lastTopLine = rubik["Top"][2]
    firstColumnRight = [rubik["Right"][i][2] for i in range(3)]
    lastBottomLine = rubik["Bottom"][2]
    lastColumnLeft = [rubik["Left"][i][0] for i in range(3)]

    rubik["Top"][2] = lastColumnLeft
    for i in range(3):
        rubik["Right"][i][2] = lastTopLine[i]
    rubik["Bottom"][2] = firstColumnRight
    for i in range(3):
        rubik["Left"][i][0] = lastBottomLine[i]


def moveLeftReverse(rubik, side):
    rl = 0
    lastColumnFront = [rubik["Front"][i][rl] for i in range(3)]
    lastColumnTop = [rubik["Top"][i][rl] for i in range(3)]
    lastColumnBack = [rubik["Back"][i][2] for i in range(3)]
    lastColumnBottom = [rubik["Bottom"][i][rl] for i in range(3)]

    for i in range(3):
        rubik["Front"][i][rl] = lastColumnBottom[i]
    tmp = 0
    for i in range(2, -1, -1):
        rubik["Top"][tmp][rl] = lastColumnFront[i]
        tmp +=1
    for i in range(3):
        rubik["Back"][i][2] = lastColumnTop[i]
    tmp = 0
    for i in range(2, -1, -1):
        rubik["Bottom"][tmp][rl] = lastColumnBack[i]
        tmp += 1

    rotateReverse(rubik["Left"])


def moveRightReverse(rubik, side):
    rl = 2
    lastColumnFront = [rubik["Front"][i][rl] for i in range(3)]
    lastColumnTop = [rubik["Top"][i][rl] for i in range(3)]
    lastColumnBack = [rubik["Back"][i][0] for i in range(2, -1, -1)]
    lastColumnBottom = [rubik["Bottom"][i][rl] for i in range(3)]

    tmp = 0
    for i in range(2, -1, -1):
        rubik["Front"][tmp][rl] = lastColumnTop[i]
        tmp +=1
    tmp = 0
    for i in range(2, -1, -1):
        rubik["Top"][i][rl] = lastColumnBack[i]
        tmp += 1
    tmp = 0
    for i in range(2, -1, -1):
        rubik["Back"][tmp][0] = lastColumnBottom[i]
        tmp += 1
    for i in range(3):
        rubik["Bottom"][i][rl] = lastColumnFront[i]

    rotateReverse(rubik["Right"])


def moveTopReverse(rubik, direction):
    ud = 0
    rotate(rubik["Top"])

    firstRowBack = rubik["Back"][ud]
    firstRowLeft = rubik["Left"][ud]
    firstRowFront = rubik["Front"][ud]
    firstRowRight = rubik["Right"][ud]

    rubik["Back"][ud] = firstRowRight
    rubik["Left"][ud] = firstRowBack
    rubik["Front"][ud] = firstRowLeft
    rubik["Right"][ud] = firstRowFront


def moveBottomReverse(rubik, direction):
    rotateReverse(rubik["Bottom"])

    firstRowBack = rubik["Back"][2]
    firstRowLeft = rubik["Left"][2]
    firstRowFront = rubik["Front"][2]
    firstRowRight = rubik["Right"][2]

    rubik["Back"][2] = firstRowLeft
    rubik["Left"][2] = firstRowFront
    rubik["Front"][2] = firstRowRight
    rubik["Right"][2] = firstRowBack
