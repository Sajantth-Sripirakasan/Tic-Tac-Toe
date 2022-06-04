from random import *

def displayBoard(board):
    for i in range (3):
        print(board[i][0], board[i][1], board[i][2])

def checkRowWin(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                count += 1
        if count == 3:
            return True
        else:
            count = 0
    return False

def checkColumnWin(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[j][i] == 'X':
                count += 1
        if count == 3:
            return True
        else:
            count = 0
    return False

def checkDiagonalWin(board):
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return True
    if board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
        return True
    return False

def checkPotentialRowWin(board, turn):
    count = 0
    notORow = 10
    notOColumn = 10

    for i in range(3):
        for j in range(3):
            if board[i][j] == turn:
                count += 1
            else:
                notORow = i
                notOColumn = j   
        if count == 2:
            if board[notORow][notOColumn] == '-':
                board[notORow][notOColumn] = 'O'
                return True, board
        else:
            count = 0
    return False, board

def checkPotentialColumnWin(board, turn):
    count = 0
    notORow = 10
    notOColumn = 10

    for i in range(3):
        for j in range(3):
            if board[j][i] == turn:
                count += 1
            else:
                notORow = j
                notOColumn = i   
                
        if count == 2:
            if board[notORow][notOColumn] == '-':
                board[notORow][notOColumn] = 'O'
                return True, board
        else:
            count = 0
    return False, board

def checkPotentialDiagonalWin(board, turn):
    count = 0
    notORow = 10
    notOColumn = 10

    if board[0][0] == turn:
        count += 1
    else:
        notORow = 0
        notOColumn = 0
    if board[1][1] == turn:
        count += 1
    else:
        notORow = 1
        notOColumn = 1
    if board[2][2] == turn:
        count += 1
    else:
        notORow = 2
        notOColumn = 2
    
    if count == 2:
        if board[notORow][notOColumn] == '-':
            board[notORow][notOColumn] = 'O'
            return True, board
    
    count = 0
    if board[2][0] == turn:
        count += 1
    else:
        notORow = 2
        notOColumn = 0
    if board[1][1] == turn:
        count += 1
    else:
        notORow = 1
        notOColumn = 1
    if board[0][2] == turn:
        count += 1
    else:
        notORow = 0
        notOColumn = 2
    
    if count == 2:
        if board[notORow][notOColumn] == '-':
            board[notORow][notOColumn] = 'O'
            return True, board
    
    return False, board 

def yourTurn(board):
    valid = False
    isWin = False
    while not valid:
        print("What position would you like to place your marker?")
        row = int(input()) - 1
        column = int(input()) - 1

        if board[row][column] != '-':
            print("There is already a marker in that spot. Please choose another spot")
        else:
            board[row][column] = 'X'
            valid = True
            if checkColumnWin(board) or checkRowWin(board) or checkDiagonalWin(board):
                isWin = True
                return board, 'X', isWin
    return board, 'O', isWin
    

def CPUTurn(board):
    isWin, board = checkPotentialRowWin(board, 'O')
    if isWin:
        return board, 'O', isWin
    else:
        isWin, board = checkPotentialColumnWin(board, 'O')
        if isWin:
            return board, 'O', isWin
        else:
            isWin, board = checkPotentialDiagonalWin(board, 'O')
            if isWin:
                return board, 'O', isWin
    
    # Start Checking for potential User Wins
    madeMove, board = checkPotentialRowWin(board, 'X')
    if madeMove:
        return board, 'X', isWin
    else:
        madeMove, board = checkPotentialColumnWin(board, 'X')
        if madeMove:
            return board, 'X', isWin
        else:
            madeMove, board = checkPotentialDiagonalWin(board, 'X')
            if madeMove:
                return board, 'X', isWin
    valid = False
    while not valid:
        row = randint(0, 2)
        col = randint(0, 2)
        if board[row][col] == '-':
            board[row][col] = 'O'
            return board, 'X', isWin

def main():
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    turn = 'X'
    isGameOver = False

    print("Welcome to Tic-Tac-Toe!")
    print()

    print("Each position of the board will be represented by its row and column. If you wish to place your marker at a specific spot,")
    print("please enter the corresponding row and column of that position on the board (i.e. top-left will be 1, 1 and top right is 1, 3)")

    print()
    print("You are X and the CPU is O")
    print("Now that you know how to play, let's begin")

    while not isGameOver:
        if turn == 'X':
            print("Your turn")
        else:
            print("CPU's turn")
        displayBoard(board)
        print()

        if turn == 'X':
            board, turn, isGameOver = yourTurn(board)
            print()
        else:
            board, turn, isGameOver = CPUTurn(board)
        
        if not any('-' in x for x in board):
            displayBoard(board)
            isGameOver = True
            print("The game has ended in a draw")
        elif isGameOver:
            displayBoard(board)
            if turn == 'X':
                print("CONGRATULATIONS! YOU WON!")
            elif turn == 'O':
                print("The CPU has won. Better luck next time")


main()