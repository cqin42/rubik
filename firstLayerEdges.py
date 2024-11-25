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

def firstLayerEdge(rubik):
    for e in rubik:
        for j in range(len(rubik[e])):
            for k in range(len(rubik[e][j])):
                if "".join(str(rubik[e][j][k][p][0]) for p in rubik[e][j][k]) == "6":
                    print(e, "x =",k,"y=",j)
