import random


def DrawBoard(board):
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print('----------')
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print('----------')
    print(" " + board[1] + " | " + board[2] + " | " + board[3])

def inputPlayerLetter():
    letter = " "
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()
    if letter == "X":
        return ['X', 'O']
    else:
        return ['O', 'X']

def chooseDifficulty():
    """Let the player choose the difficulty level"""
    difficulty = ""
    while difficulty not in ['1', '2', '3']:
        print("\nChoose difficulty:")
        print("1 - Easy (Random moves)")
        print("2 - Medium (Smart strategy)")
        print("3 - Hard (Unbeatable AI)")
        difficulty = input("Enter 1, 2, or 3: ")
    return int(difficulty)

def WhoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    print("Do you want to play again (yes or no)")
    answer = input().lower()
    return answer.startswith('y')


def MakeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or  # top
            (board[4] == letter and board[5] == letter and board[6] == letter) or  # middle
            (board[1] == letter and board[2] == letter and board[3] == letter) or  # bottom
            (board[7] == letter and board[4] == letter and board[1] == letter) or  # left
            (board[8] == letter and board[5] == letter and board[2] == letter) or  # center v
            (board[9] == letter and board[6] == letter and board[3] == letter) or  # right
            (board[7] == letter and board[5] == letter and board[3] == letter) or  # diagonal
            (board[1] == letter and board[5] == letter and board[9] == letter))  # diagonal


def getBoardCopy(board):
    return board.copy()

def isSpaceFree(board, move):
    if not board[move] == 'X' and not board[move] == 'O':
        return True
    else:
        return False

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move(1-9)')
        move = input()
    return int(move)

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


# EASY DIFFICULTY - Random moves
def getComputerMoveEasy(board):
    """Makes completely random moves"""
    possibleMoves = []
    for i in range(1, 10):
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    return random.choice(possibleMoves)


# MEDIUM DIFFICULTY - Original strategic logic
def getComputerMoveMedium(board, computerLetter):
    """Uses strategic rules: win, block, center, corners, sides"""
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Check if computer can win
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(board, i):
            MakeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Block player from winning
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(board, i):
            MakeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Take center if free
    if isSpaceFree(board, 5):
        return 5

    # Take a corner
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Take a side
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


# HARD DIFFICULTY - Minimax algorithm
def evaluatePosition(board, computerLetter, playerLetter):
    """Evaluates the board position and returns a score"""
    if isWinner(board, computerLetter):
        return 10
    elif isWinner(board, playerLetter):
        return -10
    else:
        return 0


def minimax(board, depth, isMaximizing, computerLetter, playerLetter):
    """Minimax algorithm to find the best move"""
    score = evaluatePosition(board, computerLetter, playerLetter)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth

    if isBoardFull(board):
        return 0

    if isMaximizing:
        bestScore = -1000
        for i in range(1, 10):
            if isSpaceFree(board, i):
                copy = getBoardCopy(board)
                MakeMove(copy, computerLetter, i)
                score = minimax(copy, depth + 1, False, computerLetter, playerLetter)
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 1000
        for i in range(1, 10):
            if isSpaceFree(board, i):
                copy = getBoardCopy(board)
                MakeMove(copy, playerLetter, i)
                score = minimax(copy, depth + 1, True, computerLetter, playerLetter)
                bestScore = min(score, bestScore)
        return bestScore


def getComputerMoveHard(board, computerLetter, playerLetter):
    """Uses minimax algorithm to find the optimal move"""
    bestScore = -1000
    bestMove = None

    for i in range(1, 10):
        if isSpaceFree(board, i):
            copy = getBoardCopy(board)
            MakeMove(copy, computerLetter, i)
            score = minimax(copy, 0, False, computerLetter, playerLetter)

            if score > bestScore:
                bestScore = score
                bestMove = i

    return bestMove


def getComputerMove(board, computerLetter, playerLetter, difficulty):
    """Routes to the appropriate AI based on difficulty"""
    if difficulty == 1:
        return getComputerMoveEasy(board)
    elif difficulty == 2:
        return getComputerMoveMedium(board, computerLetter)
    else:  # difficulty == 3
        return getComputerMoveHard(board, computerLetter, playerLetter)


def ticTacToe():
    while True:
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        difficulty = chooseDifficulty()
        turn = WhoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                DrawBoard(theBoard)
                move = getPlayerMove(theBoard)
                MakeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    DrawBoard(theBoard)
                    print('Congrats you are the winner!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        DrawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    turn = 'computer'

            else:
                # Computer's move based on difficulty
                if difficulty == 3:
                    print("Computer is thinking...")
                move = getComputerMove(theBoard, computerLetter, playerLetter, difficulty)
                MakeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    DrawBoard(theBoard)
                    print('The computer has beaten you, you lost!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        DrawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    turn = 'player'

        if not playAgain():
            print('See you soon again!')
            break


ticTacToe()