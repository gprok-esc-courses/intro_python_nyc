
board = [['-' for i in range(3)] for j in range(3)]
print(board)
player = 'X'

# loop until someone wins 
# (but I don't know winner yet, so repeat forever)
while True:
    # print the board
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

    # ask current user to play
    r = int(input("Give row: "))
    c = int(input("Give col: "))
    if r >= 0 and r < 3 and c >=0 and c < 3 and board[r][c] == '-':
        board[r][c] = player 
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    else:
        print("invalid row or col or cell already used")

    # check for winner
    # check for tie