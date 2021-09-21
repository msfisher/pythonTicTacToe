# command line tick tac toe for students to learn testing
import random

# Global variables
difficultyLevel = 0  # computer chooses randomly (0) or plays intelligently (1)
gameBoard = {'0': ' ', '1': ' ', '2': ' ',
             '3': ' ', '4': ' ', '5': ' ',
             '6': ' ', '7': ' ', '8': ' ',
             }
userTurn = True  # keep track of who's turn it is (True = human)


# method to print the game board
def printGameBoard():
    global gameBoard
    print(gameBoard['0'] + '|' + gameBoard['1'] + '|' + gameBoard['2'])
    print('-+-+-')
    print(gameBoard['3'] + '|' + gameBoard['4'] + '|' + gameBoard['5'])
    print('-+-+-')
    print(gameBoard['6'] + '|' + gameBoard['7'] + '|' + gameBoard['8'])


def getRandomAnswer():
    global gameBoard
    # get a random square, see if there is something there, if not then add an O
    # if there is something there then keep selecting random squares
    # can be a time bottleneck
    while (True):
        indexValue = random.randint(0, len(gameBoard) - 1)
        if (gameBoard[str(indexValue)] == ' '):
            gameBoard[str(indexValue)] = 'O'
            break


def getSmartAnswer():
    global gameBoard
    user = input()
    gameBoard[user] = 'O'


# Game Loop
for x in range(0, 9):
    # print the game board
    printGameBoard()
    print()

    # if it is user's turn then ask where they would like to place an X
    if (userTurn):
        print('Where would you like to placee an X (0-8): ', end=' ')
        userAnswer = input()
        gameBoard[userAnswer] = 'X'
        userTurn = False
    else:
        # computers turn so check difficulty level whether you just want to randomly choose
        # a square or intelligently choose a square
        if (difficultyLevel == 0):
            computerAnswer = getRandomAnswer()
        else:
            computerAnswer = getSmartAnswer()
        userTurn = True

    # determine if anyone has won, if not then continue play
