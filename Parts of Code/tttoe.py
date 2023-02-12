import random

def check_board(board):
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    # check if board is full
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return None
    return 'Tie'

def print_board(board):
    print(" {} | {} | {} ".format(board[0][0], board[0][1], board[0][2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[1][0], board[1][1], board[1][2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[2][0], board[2][1], board[2][2]))

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    board[1][1] = 'X'
    print_board(board)

    while True:
        move = int(input("Your move (1-9): "))
        row, col = (move - 1) // 3, (move - 1) % 3
        if board[row][col] != ' ':
            print("Invalid move!")
            continue
        board[row][col] = 'O'
        result = check_board(board)
        if result != None:
            break
        print_board(board)

        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if board[row][col] == ' ':
                break
        board[row][col] = 'X'
        result = check_board(board)
        if result != None:
            break
        print_board(board)

    print("Result:", result)

tic_tac_toe()
