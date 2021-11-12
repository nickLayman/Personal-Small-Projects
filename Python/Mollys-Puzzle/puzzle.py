'''
puzzle has 9 pieces
must be in a square
each piece has half of 4 different animals
butts and heads must line up correctly on all animals

positive is head
negative is butt

1 = raccoon
2 = fox
3 = skunk
4 = porcupine

solution:
[   s   ]  [   r   ]  [   s   ]
[p    -f]  [f     p]  [-p    r]
[  -r   ]  [   s   ]  [   f   ]

[   r   ]  [  -s   ]  [  -f   ]
[f    -p]  [p    -r]  [r     p]
[   s   ]  [  -f   ]  [  -s   ]

[  -s   ]  [   f   ]  [   s   ]
[r     p]  [-p    r]  [-r    f]
[   f   ]  [  -s   ]  [   p   ]



solution in numbers (actual readout):
[   3   ]  [   1   ]  [   3   ]
[4    -2]  [2     4]  [-4    1]
[  -1   ]  [   3   ]  [   2   ]

[   1   ]  [  -3   ]  [  -2   ]
[2    -4]  [4    -1]  [1     4]
[   3   ]  [  -2   ]  [  -3   ]

[  -3   ]  [   2   ]  [   3   ]
[1     4]  [-4    1]  [-1    2]
[   2   ]  [  -3   ]  [   4   ]

squares labeled left to right top to bottom according to pic
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

animals labeled clockwise from top on each square
[   1   ]
[4     2]
[   3   ]
'''

S1 = [4, -3, 1, -2]
S2 = [-3, 4, 2, 1]
S3 = [3, 2, 1, 4]
S4 = [3, -2, -1, 4]
S5 = [-4, 2, 1, -3]
S6 = [1, 2, -4, 3]
S7 = [2, 4, -1, 3]
S8 = [2, 1, -4, 3]
S9 = [-3, -1, -2, 4]

allSquares = [S1, S2, S3, S4, S5, S6, S7, S8, S9]
board = allSquares.copy()


def rotatecw(piece):
    whatToReturn = [piece[3], piece[0], piece[1], piece[2]]
    return whatToReturn


def rotateAllcw(whatToRotate):
    toReturn = whatToRotate.copy()
    for ind in range(len(toReturn)):
        toReturn[ind] = rotatecw(toReturn[ind])
    return toReturn


everyPossibleSquare = allSquares.copy()
oneRotation = rotateAllcw(allSquares.copy())
twoRotations = rotateAllcw(oneRotation.copy())
threeRotations = rotateAllcw(twoRotations.copy())

for square in oneRotation:
    everyPossibleSquare.append(square)
for square in twoRotations:
    everyPossibleSquare.append(square)
for square in threeRotations:
    everyPossibleSquare.append(square)


def check(pieceplaced):
    checks = {
        0: True,
        1: board[0][1] + board[1][3] == 0,
        2: board[1][1] + board[2][3] == 0,
        3: board[0][2] + board[3][0] == 0,
        4: board[1][2] + board[4][0] == 0 and board[3][1] + board[4][3] == 0,
        5: board[2][2] + board[5][0] == 0 and board[4][1] + board[5][3] == 0,
        6: board[3][2] + board[6][0] == 0,
        7: board[4][2] + board[7][0] == 0 and board[6][1] + board[7][3] == 0,
        8: board[5][2] + board[8][0] == 0 and board[7][1] + board[8][3] == 0
    }
    return checks[pieceplaced]


def printboard():
    '''
    [   1   ]
    [4     2]
    [   3   ]
    '''
    print(f"[   {board[0][0]}   ]  [   {board[1][0]}   ]  [   {board[2][0]}   ]")
    print(f"[{board[0][3]}    {board[0][1]}]  [{board[1][3]}     {board[1][1]}]  [{board[2][3]}    {board[2][1]}]")
    print(f"[  {board[0][2]}   ]  [   {board[1][2]}   ]  [   {board[2][2]}   ]\n")

    print(f"[   {board[3][0]}   ]  [  {board[4][0]}   ]  [  {board[5][0]}   ]")
    print(f"[{board[3][3]}    {board[3][1]}]  [{board[4][3]}    {board[4][1]}]  [{board[5][3]}     {board[5][1]}]")
    print(f"[   {board[3][2]}   ]  [  {board[4][2]}   ]  [  {board[5][2]}   ]\n")

    print(f"[  {board[6][0]}   ]  [   {board[7][0]}   ]  [   {board[8][0]}   ]")
    print(f"[{board[6][3]}     {board[6][1]}]  [{board[7][3]}    {board[7][1]}]  [{board[8][3]}    {board[8][1]}]")
    print(f"[   {board[6][2]}   ]  [  {board[7][2]}   ]  [   {board[8][2]}   ]")


if __name__ == '__main__':
    placeindex = 0
    squareindeces = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    while 0 <= placeindex < 9:
        while squareindeces[placeindex] < 36:
            noRepeats = True
            for ind in range(placeindex):
                if (board[ind] == everyPossibleSquare[squareindeces[placeindex]] or
                        board[ind] == (rotatecw(everyPossibleSquare[squareindeces[placeindex]])) or
                        board[ind] == (rotatecw(rotatecw(everyPossibleSquare[squareindeces[placeindex]]))) or
                        board[ind] == (rotatecw(rotatecw(rotatecw(everyPossibleSquare[squareindeces[placeindex]]))))):
                    noRepeats = False
            if noRepeats:
                board[placeindex] = everyPossibleSquare[squareindeces[placeindex]]
            if check(placeindex):
                placeindex += 1
            else:
                squareindeces[placeindex] += 1
            if placeindex == 9:
                printboard()
        squareindeces[placeindex] = 0
        placeindex -= 1
        squareindeces[placeindex] += 1
        if squareindeces[0] == 0 or squareindeces[0] == 35:
            if squareindeces[0] == 0 and squareindeces[1] >= 33:
                print(0)
    print(squareindeces)
