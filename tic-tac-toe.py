############################################################
# Project 1: Tic-Tac-Toe
# By Aiman Aisamuddin bin Ab Ghapar
# Data Analyst July 2022 Intake
# Last Updated: 06/07/2022
############################################################
#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# import libraries
import unittest

# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# use to update the gameboard with the user input
def markBoard(position, mark):
    board[int(position)] = mark
    # casted position with 'int' type to avoid creating new key
    # since key in board is in 'int' but the input is of type 'str'
    return board


# print the game board as described at the top of this code skeleton
def printBoard():
    # create a list of 1-9
    list = [i for i in range(1, 10)]
    # replace the list to printed with 'X' and 'O' 
    for key, value in board.items():
        if value != " ":
            list[int(key) - 1] = value
            
    # printing the tic-tac-toe board
    print('Current Board: \n\n' +
    ' ' + str(list[0]) + ' | ' + str(list[1]) +  ' | '  + str(list[2])  + '\n' +
    ' --------- \n' +
    ' ' + str(list[3]) + ' | ' + str(list[4]) +  ' | '  + str(list[5]) + '\n' +
    ' --------- \n' +
    ' ' + str(list[6]) + ' | ' + str(list[7]) +  ' | '  + str(list[8]) + '\n')
    return # nothing to return since we use this function to print the board only



# check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    # return false if the input is not a number
    # and break from the while loop if it is a number
    while True:
        try:
            n = int(position)
            break
        except ValueError:
            return False
    # check if the input is between 1-9 inclusively
    if n > 9 or n < 1:
        return False
    # to check if the input position is already filled
    elif board[n] == "X" or board[n] == "O":
        return False
    else:
        return True



# list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]

# implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    # create an empty list
    # this index list and for loop are used to list out all the position where
    # the current player has marked
    index = []
    for key, value in board.items():
        if value == player:
            index.append(int(key))
    # to compared whether any of the list in the winCombinations
    # is a subset of the index list
    flag = False
    for list in winCombinations:
        # if one of the list in winCombinations is a subset of 
        # index list, then return True
        if all(x in index for x in list):
            flag = True
            break
    return flag


# implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    flag = True
    for value in board.values():
        # if there's no " " in the values of the board dictionary
        # return True (it's full)
        if value == " ":
            flag = False
            break
    return flag



#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

# Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User


# initialize the restart game loop
# this loop will keep running until the restart_game is False 
restart_game = True
while restart_game:
    # entry point of the whole program
    # initialize the printed board
    print('Game started: \n\n' +
        ' 1 | 2 | 3 \n' +
        ' --------- \n' +
        ' 4 | 5 | 6 \n' +
        ' --------- \n' +
        ' 7 | 8 | 9 \n')
    
    # initialize the gameEnded for the while loop 
    gameEnded = False
    
    # initialize the player, "X" always start first
    currentTurnPlayer = 'X'
    
    # initialize the board
    board = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
        }
    
    # this loop will keep running until there is a winner or the board is full 
    while not gameEnded:
        # ask for position input from player
        move = input(currentTurnPlayer + "'s turn, input: ")
        
        # this while loop will check the input and will keep asking until the input is valid
        while validateMove(move) == False:
            move = input(currentTurnPlayer + "'s turn, invalid input. Please try again, input: ")
        
        # mark and print the board
        markBoard(move, currentTurnPlayer)
        printBoard()
        
        # check if there is a winner
        # must be careful to check for the winner first before checking the board is full
        # since there might still be a winner although the board is full
        if checkWin(currentTurnPlayer) or checkFull() == True:
            if checkWin(currentTurnPlayer) == True:
                print(currentTurnPlayer + " wins the game")
            else:
                print("It's a tie")
            # ended the game and break the game loop
            gameEnded = True
            break
        # if no winner or not tie, this part will switch the player
        else:
            if currentTurnPlayer == 'X':
                currentTurnPlayer = 'O'
            else:
                currentTurnPlayer = 'X'
    # end of game loop
    
    # these code will ask the player whether to play another game or no
    Y_N = input("Do you want to play another game? Y/N: ")
    
    # this while loop will keep asking the using until the input is valid
    valid_input = ["Y", "y", "N", "n"]
    while Y_N not in valid_input:
        Y_N = input("Invalid input. Please try again, Y/N: ")
    
    # if the input is 'N' or 'n' stop the game totally
    if Y_N == "N" or Y_N == "n":
        restart_game == False
        break
# end of restartgame loop
