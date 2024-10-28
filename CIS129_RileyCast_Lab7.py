# Lab 7-3 The Dice Game
# Riley Cast
# 10/27/2024
# This program plays a dice game between two players. 
# It generates random dice rolls and then determines the winner, and displays the results.

import random  

# the main function
def main():
    print()

    # initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'

    # call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    # while loop to run program again
    while endProgram == 'no':

        # populate variables
        winnersName = 'NO NAME'
        p1number = 0
        p2number = 0

        # call to rollDice
        winnersName = rollDice(p1number, p2number, playerOne, playerTwo) 

        # call to displayInfo
        displayInfo(winnersName)

        endProgram = input('Do you want to end program? (yes/no): ')


#this function gets the players names
def inputNames(playerOne, playerTwo):
    playerOne = input("Enter Player 1's name: ")
    playerTwo = input("Enter Player 2's name: ")
    return playerOne, playerTwo


#this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    if p1number > p2number:
        winnerName = playerOne
    elif p2number > p1number:
        winnerName = playerTwo
    else:
        winnerName = "TIE"

    return winnerName


#this function displays the winner
def displayInfo(winnerName):
    print(f"The winner is: {winnerName}")


# calls main
main()
