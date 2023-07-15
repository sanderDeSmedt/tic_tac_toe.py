#Tic tac toe

import random

def DrawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    # for more esthetics uncomment some parts.
    #print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print('----------')
    #print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print('----------')
    #print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " +board[3])
    #print("   |   |")

def inputPlayerLetter():
    #This function let the player decide wich letter they want to be
    #returns a list with the players letter as first item and the computers second.
    letter = " "
    while not (letter =="X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()
    if letter == "X":
        return ['X','O']
    else:
        return ['O','X']

def WhoGoesFirst():
    #Randomly choosing who goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #This function returns true if the player wants to play again.
    print("Do you want to play again (yes or no)")
    if input().lower().startswith('y'):
        return True
    elif input().lower().startswith('n'):
        return False
    else:
        print('Do you want to play again (yes or no)')

def MakeMove(board,letter,move):
    board[move] = letter
'''
def placeTaken(board,i):
    if board[i] == '':
        return False
    else:
        return True
'''
def isWinnerHorizontal(board,letter):
    #this function checks if there is a winner horizontally
    if ((board[7] == letter and board[8] == letter and board[9] == letter) or
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[1] == letter and board[2] == letter and board[3] == letter)):
        return True
    else:
        return False
def isWinnerVertical(board,letter):
    #this function checks if there is a winner vertically
    if ((board[7] == letter and board[4] == letter and board[1] == letter) or
        (board[8] == letter and board[5] == letter and board[2] == letter) or
        (board[9] == letter and board[6] == letter and board[3] == letter)):
        return True
    else:
        return False
def isWinnerDiagonal(board,letter):
    #this function checks if there is a winner diagonally
    if ((board[7] == letter and board[5] == letter and board[3] == letter) or
        (board[1] == letter and board[5] == letter and board[9] == letter)):
        return True
    else:
        return False
def isWinner(board,letter):
    #this Function implements the other isWinner... functions and sees if one of them returns True
    if isWinnerDiagonal(board,letter) or isWinnerHorizontal(board,letter) or isWinnerVertical(board,letter):
        return True
    else:
        return False
def getBoardCopy(board):
    #Makes a duplicate of the board and returns this duplicate
    dupeBoard = []
    for i in range(len(board)):
       dupeBoard.append(board[i])
    return dupeBoard

def isSpaceFree(board,move):
    #retuns wether or not the given position is free
    if not board[move] == 'X' and not board[move] == 'O':
        return True
    else:
        return False

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print('What is your next move(1-9)')
        move = input('move')
    return int(move)

def chooseRandomMoveFromList(board,moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return "No moves found"

def isFullDiagonal(board, computerLetter):
    for i in range(1,10):
        copy = getBoardCopy(board)
        MakeMove(copy,computerLetter,i)
        if not isSpaceFree(board,7) and not isSpaceFree(board,5) and not isSpaceFree(board,3):
            return False
        if not isSpaceFree(board,1) and not isSpaceFree(board,5) and not isSpaceFree(board,9):
            return False
        else:
            return True

def getComputerMove(board,computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    #This wil be the computer's thinking
    #checks wether the computer has a winning move
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(board,i):
            MakeMove(copy,computerLetter,i)
            if isWinner(copy, computerLetter):
                return i
    #if the player can win with the following move: block
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(board,i):
            MakeMove(copy,playerLetter,i)
            if isWinner(copy, playerLetter):
                return i
    # if the center is free, choose the center
    if isSpaceFree(board, 5):
        return 5
    #if the center is not free the computer will choose one of the corners
    i = 1
    #originalBoard = board
    while i <= 4:
        move = chooseRandomMoveFromList(board,[1,3,7,9])
        if isSpaceFree(board, move):
            return move
        else:
            i += 1

        #copy = getBoardCopy(originalBoard)
        #MakeMove(board,computerLetter,move)
        #if isFullDiagonal(copy, computerLetter):
        #    i +=1
        #else:
        #    return move
    #Choose on on the sides
    return chooseRandomMoveFromList(board,[2,4,6,8])

def isBoardFull(board):
    #returns True if all the positions are taken els returns False
    for i in range(len(board)):
        if isSpaceFree(board,i):
            return False
        else:
            return True

def goodMove(board, playerletter,next):
    good_move = True

    while good_move:
        move = getPlayerMove(board)
        if isSpaceFree(board, move):
            MakeMove(board, playerletter, move)
            DrawBoard(board)
            good_move = False
            turn = next
            return turn
        else:
            print('invalid move, try again')

def ticTacToe():
    while True:
        theBoard = [' ']*10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = WhoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                DrawBoard(theBoard)
                goodMove(theBoard,playerLetter, 'computer')
                if isWinner(theBoard,playerLetter):
                    DrawBoard(theBoard)
                    print('Congrats you are the winner')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        DrawBoard(theBoard)
                        print('The game is a tie')
                        break
                    turn = 'computer'

            else:
                #computer's move
                move = getComputerMove(theBoard,computerLetter)

                if isSpaceFree(theBoard, move):
                    MakeMove(theBoard, computerLetter, move)
                DrawBoard(theBoard)
                goodMove(theBoard, computerLetter, 'player')
                """
                good_move = True
                while good_move:
                    move = getPlayerMove(theBoard)
                    if isSpaceFree(theBoard, move):
                        MakeMove(theBoard,playerLetter,move)
                        good_move = False
                    else:
                        print('invalid move, try again')
                """
                print(turn)
                if isWinner(theBoard,computerLetter):
                    DrawBoard(theBoard)
                    print('The computer has beaten you, you lost!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        print('the game is a tie!')
                        break
                    turn = 'player'
        if not playAgain():
            print('See you soon again!')
            break
ticTacToe()
