
lastMarble = 25

players = 9

board = [-1 for i in range(lastMarble)]

board[0], board[1], board[2] = 0 , 2, 1

currMarble = 2
toAdd = 3
nextIdx = 3

currPlayer = 1
scores = {}

while currMarble <= 22:
    if board[nextIdx] == -1:
        board[nextIdx] = toAdd
        currMarble = toAdd
        toAdd += 1
        nextIdx = 1
    else:
        board.insert(nextIdx, toAdd)
        toAdd += 1
        nextIdx += 2

    currMarble += 1
    currPlayer += 1


print(board)
    
print(scores)