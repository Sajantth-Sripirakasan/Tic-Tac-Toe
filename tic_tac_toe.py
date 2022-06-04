from random import *

# Used to display the current board
def displayBoard(board):
    for i in range (3):
        print(board[i][0], board[i][1], board[i][2]) # prints each row on one line

# Used to check if the user has won on a row
def checkRowWin(board):
    count = 0   # Used to keep track of how many X's are in the current row
    for i in range(3):  # Goes through the rows
        for j in range(3):  # Goes through the columns
            if board[i][j] == 'X': 
                count += 1  # if the current position is 'X', count is increased by 1
        if count == 3:
            return True  # If, after going through the row, count is 3, then the user wins and the function returns True
        else:
            count = 0  # If count is not 3, then the user has not won on this row, so count is reset to 0 and it goes to the next row
    return False # If, after going through all the rows, count is never 3, then the user has not won on a row and False is returned

# Used to check if the user has won on a Column
def checkColumnWin(board):
    count = 0  # Used to keep track of how many X's are in the current column
    for i in range(3):  # Goes through the columns
        for j in range(3):  # Goes through the rows
            if board[j][i] == 'X':
                count += 1  # if the current position is 'X', count is increased by 1
        if count == 3:
            return True  # If, after going through the column, count is 3, then the user wins and the function returns True
        else:
            count = 0  # If count is not 3, then the user has not won on this column, so count is reset to 0 and it goes to the next column
    return False # If, after going through all the columns, count is never 3, then the user has not won on a column and False is returned

# Used to check if the user has won on a Diagonal
def checkDiagonalWin(board):
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return True  # If all indexes from the main diagonal are 'X', then True is returned
    if board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
        return True  # If all indexes from the other diagonal are 'X', then True is returned
    return False  # Otherwise, the user has not won on a diagonal and False is returned

# Used to check if either the CPU or the user are 1 move away from a win on a row
# This function is used during the CPU's turn to determine if the CPU can win or block a potential win from the user on this turn
# The function takes in the board, as well as the turn (either 'O' or 'X')
def checkPotentialRowWin(board, turn):
    count = 0  # Used to keep track of how many O's or X's are in the current row
    notORow = -1  # Used to keep track of the row of the index that does not have an 'O'
    notOColumn = -1  # Used to keep track of the column of the index that does not have an 'O'

    for i in range(3):  # Goes through the rows
        for j in range(3):  # Goes through the columns
            if board[i][j] == turn: 
                count += 1   # if the current position is the same as turn, count is increased by 1
            else:
                # Otherwise notORow and notOColumn are given the values of the row and column of the current index
                notORow = i   
                notOColumn = j   
        if count == 2:
            if board[notORow][notOColumn] == '-':
                # If count is 2 and the remaining index is a blank space, that means the CPU can win or block a user win on this turn
                board[notORow][notOColumn] = 'O' # the remaining index on the board is set to 'O'
                return True, board # returns True (if the CPU won or made a move) and the board
        else:
            count = 0 # If there are no potential wins on this row, count is set to 0 and it moves to the next row
    return False, board # If there are no potential row wins, False and board are returned

# Used to check if either the CPU or the user are 1 move away from a win on a column
# This function is used during the CPU's turn to determine if the CPU can win or block a potential win from the user on this turn
# The function takes in the board, as well as the turn (either 'O' or 'X')
def checkPotentialColumnWin(board, turn):
    count = 0  # Used to keep track of how many O's or X's are in the current column
    notORow = -1  # Used to keep track of the row of the index that does not have an 'O'
    notOColumn = -1  # Used to keep track of the column of the index that does not have an 'O'

    for i in range(3): # Goes through the columns
        for j in range(3): # Goes through the rows
            if board[j][i] == turn:
                count += 1  # if the current position is the same as turn, count is increased by 1
            else:
                # Otherwise notORow and notOColumn are given the values of the row and column of the current index
                notORow = j
                notOColumn = i   
                
        if count == 2:
            if board[notORow][notOColumn] == '-':
                # If count is 2 and the remaining index is a blank space, that means the CPU can win or block a user win on this turn
                board[notORow][notOColumn] = 'O'  # the remaining index on the board is set to 'O'
                return True, board  # returns True (if the CPU won or made a move) and the board
        else:
            count = 0  # If there are no potential wins on this column, count is set to 0 and it moves to the next column
    return False, board # If there are no potential column wins, False and board are returned

# Used to check if either the CPU or the user are 1 move away from a win on a diagonal
# This function is used during the CPU's turn to determine if the CPU can win or block a potential win from the user on this turn
# The function takes in the board, as well as the turn (either 'O' or 'X')
def checkPotentialDiagonalWin(board, turn):
    count = 0  # Used to keep track of how many O's or X's are in the current diagonal
    notORow = -1  # Used to keep track of the row of the index that does not have an 'O'
    notOColumn = -1  # Used to keep track of the column of the index that does not have an 'O'

    # This first group of if-else statements are used to check the main diagonal
    # count is increased by 1 for every index on the diagonal that is equal to turn
    # Otherwise notORow and notOColumn are given the values of the row and column of the current index
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
    
    # After checking the main diagonal indexes
    if count == 2:
        if board[notORow][notOColumn] == '-':
            # If count is 2 and the remaining index is a blank space, that means the CPU can win or block a user win on this turn
            board[notORow][notOColumn] = 'O' # the remaining index on the board is set to 'O'
            return True, board  # returns True (if the CPU won or made a move) and the board
    
    count = 0 # count is reset to 0

    # Now the remainder of this function checks the other diagonal
    # count is increased by 1 for every index on the diagonal that is equal to turn
    # Otherwise notORow and notOColumn are given the values of the row and column of the current index
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
    
    # After checking the other diagonal indexes
    if count == 2:
        if board[notORow][notOColumn] == '-':
            # If count is 2 and the remaining index is a blank space, that means the CPU can win or block a user win on this turn
            board[notORow][notOColumn] = 'O' # the remaining index on the board is set to 'O'
            return True, board  # returns True (if the CPU won or made a move) and the board
    
    return False, board # If there are no potential diagonal wins, False and board are returned

# This function is used for the user's turn
def yourTurn(board):
    valid = False # A boolean variable used to see if a valid move has been played
    isWin = False # A boolean variable used to see if the user has won

    # This loop will keep repeating until a valid move has been played
    while not valid:
        print("What position would you like to place your marker?") # Asks the user which index the user would like to place their marker
        row = int(input()) - 1 # Gets input from the user for the row
        column = int(input()) - 1  # Gets input from the user for the column

        if board[row][column] != '-': # If the index chosen by the user is not blank
            print("There is already a marker in that spot. Please choose another spot") # The user is asked to provide another index
        else:
            # If the index chosen by the user is blank
            board[row][column] = 'X' # That index on the board is set to 'X'
            valid = True # the boolean variable valid is set to True
            if checkColumnWin(board) or checkRowWin(board) or checkDiagonalWin(board): # Checks to see if the user has won
                isWin = True # If the user has won, isWin is set to True
                return board, 'X', isWin  # board, 'X' and isWin(True) are returned
    return board, 'O', isWin # If the user has not won, board, 'O', and isWin(False) are returned
    
# This function is used for the CPU's turn
# It will use some of the other functions to determine where to place the marker 
def CPUTurn(board):
    # Start to check for potential wins
    isWin, board = checkPotentialRowWin(board, 'O') # Checks if there is a potential row win
    if isWin:
        return board, 'O', isWin # If the CPU has won on a row, board, 'O', and isWin(True) are returned
    else:
        isWin, board = checkPotentialColumnWin(board, 'O') # Checks if there is a potential column win
        if isWin:
            return board, 'O', isWin # If the CPU has won on a column, board, 'O', and isWin(True) are returned
        else:
            isWin, board = checkPotentialDiagonalWin(board, 'O') # Checks if there is a potential diagonal win
            if isWin:
                return board, 'O', isWin # If the CPU has won on a diagonal, board, 'O', and isWin(True) are returned
    
    # If there are no potential CPU wins, start checking for potential user wins to block
    madeMove, board = checkPotentialRowWin(board, 'X') # Checks if there is a potential row win for the user
    if madeMove:
        return board, 'X', isWin # If the CPU has made a move to block a user row win, board, 'X', and isWin(False) are returned
    else:
        madeMove, board = checkPotentialColumnWin(board, 'X') # Checks if there is a potential column win for the user
        if madeMove:
            return board, 'X', isWin # If the CPU has made a move to block a user column win, board, 'X', and isWin(False) are returned
        else:
            madeMove, board = checkPotentialDiagonalWin(board, 'X') # Checks if there is a potential diagonal win for the user
            if madeMove:
                return board, 'X', isWin # If the CPU has made a move to block a user diagonal win, board, 'X', and isWin(False) are returned
    
    # If no move has been made yet
    valid = False # A boolean variable used to see if a valid move has been played

    # This loop will keep repeating until a valid move has been played
    while not valid:
        row = randint(0, 2) # Finds a random number between 0 and 2 for the row
        col = randint(0, 2) # Finds a random number between 0 and 2 for the column
        if board[row][col] == '-':
            board[row][col] = 'O' # If the random index is blank, then it is set to 'O'
            return board, 'X', isWin # board, 'X' and isWin(False) are returned

def main():
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]  # start with and empty board
    turn = 'X'  # The User is X and they will go first
    isGameOver = False  # setting a boolean variable to check when the game is over

    # A welcome message explaining how to play
    print("Welcome to Tic-Tac-Toe!")
    print() # I use these print() statements just to create space in the outputs so it looks neat

    print("Each position of the board will be represented by its row and column. If you wish to place your marker at a specific spot,")
    print("please enter the corresponding row and column of that position on the board (i.e. top-left will be 1, 1 and top right is 1, 3)")

    print()
    print("You are X and the CPU is O")
    print("Now that you know how to play, let's begin")

    # Keeps repeating until the game is over
    while not isGameOver:
        # Show which player's turn it is
        if turn == 'X':
            print("Your turn")
        else:
            print("CPU's turn")
        displayBoard(board) # Displays the current board
        print() 

        if turn == 'X':
            board, turn, isGameOver = yourTurn(board) # Calls the yourTurn() function if it is the user's turn 
            print()
        else:
            board, turn, isGameOver = CPUTurn(board)  # If it is not the user's turn, it calls the CPUTurn function 
        
        # In the case of a draw:
        if not any('-' in x for x in board):  # Checks if there are any remaining blank spaces on the board
            displayBoard(board)
            isGameOver = True  # Sets isGameOver to True so it can break out of the while loop
            print("The game has ended in a draw")  # Game over statement declaring the game a draw
        # In the case of a win by either side   
        elif isGameOver:
            displayBoard(board)
            # If the user won
            if turn == 'X':
                print("CONGRATULATIONS! YOU WON!")  # Prints statement declaring the user as the winner
            # If the CPU won
            elif turn == 'O':
                print("The CPU has won. Better luck next time") # Prints statement declaring the CPU as the winner


main()