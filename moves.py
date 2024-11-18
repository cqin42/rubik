import numpy as np

# lst = [
#         "F", ok
#         "R",
#         "U",
#         "B",
#         "L",
#         "D",

#         "F’",
#         "R’",
#         "U’",
#         "B’",
#         "L’",
#         "D’",

#         "F2",
#         "R2",
#         "U2",
#         "B2",
#         "L2",
#         "D2",
#     ]

def moveF(rubik, direction):
    rubik[direction] = np.rot90(rubik[direction], 3)
    lastTopLine = rubik["Top"][2]
    firstColumnRight = [rubik["Right"][i][0] for i in range(3)]
    lastBottomLine = rubik["Bottom"][2]
    lastColumnLeft = [rubik["Left"][i][2] for i in range(3)]

    rubik["Top"][2] = lastColumnLeft
    for i in range (3):
        rubik["Right"][i][0] = lastTopLine[i]
    rubik["Bottom"][2] = firstColumnRight
    for i in range (3):
        rubik["Left"][i][0] = lastBottomLine[i]


def moveT(rubik, direction):
    rubik[direction] = np.rot90(rubik[direction], 3)
    
    firstRowBack = rubik["Back"][0]
    firstRowLeft = rubik["Left"][0]
    firstRowFront = rubik["Front"][0]
    firstRowRight = rubik["Right"][0]

    rubik["Back"][0] = firstRowRight
    rubik["Left"][0] = firstRowBack
    rubik["Front"][0] = firstRowLeft
    rubik["Right"][0] = firstRowFront

def moveB(rubik, direction):
    rubik[direction] = np.rot90(rubik[direction], 1)

    lastRowBack = rubik["Back"][2]
    lastRowLeft = rubik["Left"][2]
    lastRowFront = rubik["Front"][2]
    lastRowRight = rubik["Right"][2]

    rubik["Back"][2] = lastRowRight
    rubik["Left"][2] = lastRowBack
    rubik["Front"][2] = lastRowLeft
    rubik["Right"][2] = lastRowFront

