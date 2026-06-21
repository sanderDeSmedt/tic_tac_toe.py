import random
import tkinter as tk
from tkinter import messagebox


# ==========================================
# AI LOGIC (Your Core Mechanics)
# ==========================================

def isSpaceFree(board, move):
    return board[move] == ' '


def isBoardFull(board):
    return ' ' not in board[1:10]


def isWinner(b, l):
    return ((b[7] == l and b[8] == l and b[9] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[1] == l and b[2] == l and b[3] == l) or
            (b[7] == l and b[4] == l and b[1] == l) or
            (b[8] == l and b[5] == l and b[2] == l) or
            (b[9] == l and b[6] == l and b[3] == l) or
            (b[7] == l and b[5] == l and b[3] == l) or
            (b[1] == l and b[5] == l and b[9] == l))


def getBoardCopy(board):
    return board.copy()


def MakeMove(board, letter, move):
    board[move] = letter


def chooseRandomMoveFromList(board, moveList):
    possibleMoves = [i for i in moveList if isSpaceFree(board, i)]
    return random.choice(possibleMoves) if possibleMoves else None


def getComputerMoveEasy(board):
    possibleMoves = [i for i in range(1, 10) if isSpaceFree(board, i)]
    return random.choice(possibleMoves)


def getComputerMoveMedium(board, computerLetter):
    playerLetter = 'O' if computerLetter == 'X' else 'X'

    for i in range(1, 10):
        if isSpaceFree(board, i):
            copy = getBoardCopy(board)
            MakeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter): return i

    for i in range(1, 10):
        if isSpaceFree(board, i):
            copy = getBoardCopy(board)
            MakeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter): return i

    if isSpaceFree(board, 5): return 5
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None: return move
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def evaluatePosition(board, computerLetter, playerLetter):
    if isWinner(board, computerLetter): return 10
    if isWinner(board, playerLetter): return -10
    return 0


def minimax(board, depth, isMaximizing, computerLetter, playerLetter, alpha, beta):
    score = evaluatePosition(board, computerLetter, playerLetter)
    if score == 10: return score - depth
    if score == -10: return score + depth
    if isBoardFull(board): return 0

    if isMaximizing:
        bestScore = -1000
        for i in range(1, 10):
            if isSpaceFree(board, i):
                copy = getBoardCopy(board)
                MakeMove(copy, computerLetter, i)
                score = minimax(copy, depth + 1, False, computerLetter, playerLetter, alpha, beta)
                bestScore = max(score, bestScore)
                alpha = max(alpha, score)
                if beta <= alpha: break
        return bestScore
    else:
        bestScore = 1000
        for i in range(1, 10):
            if isSpaceFree(board, i):
                copy = getBoardCopy(board)
                MakeMove(copy, playerLetter, i)
                score = minimax(copy, depth + 1, True, computerLetter, playerLetter, alpha, beta)
                bestScore = min(score, bestScore)
                beta = min(beta, score)
                if beta <= alpha: break
        return bestScore


def getComputerMoveHard(board, computerLetter, playerLetter):
    bestScore = -1000
    bestMove = None
    alpha, beta = -1000, 1000
    for i in range(1, 10):
        if isSpaceFree(board, i):
            copy = getBoardCopy(board)
            MakeMove(copy, computerLetter, i)
            score = minimax(copy, 0, False, computerLetter, playerLetter, alpha, beta)
            if score > bestScore:
                bestScore = score
                bestMove = i
            alpha = max(alpha, score)
    return bestMove


# ==========================================
# GUI APPLICATION
# ==========================================

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Pro Edition")

        # Game State Variables
        self.board = [' '] * 10
        self.playerLetter = 'X'
        self.computerLetter = 'O'
        self.difficulty = tk.IntVar(value=3)  # Default Hard
        self.buttons = {}

        self.setup_menu()

    def setup_menu(self):
        """Creates the initial configuration setup screen"""
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack()

        tk.Label(self.frame, text="Welcome to Tic Tac Toe!", font=('Helvetica', 16, 'bold')).pack(pady=10)

        # Difficulty Selection
        tk.Label(self.frame, text="Choose Difficulty:", font=('Helvetica', 11)).pack(anchor='w')
        tk.Radiobutton(self.frame, text="Easy (Random)", variable=self.difficulty, value=1).pack(anchor='w')
        tk.Radiobutton(self.frame, text="Medium (Strategic)", variable=self.difficulty, value=2).pack(anchor='w')
        tk.Radiobutton(self.frame, text="Hard (Unbeatable Minimax)", variable=self.difficulty, value=3).pack(anchor='w')

        # Letter Selection
        tk.Label(self.frame, text="\nChoose Your Side:", font=('Helvetica', 11)).pack(anchor='w')
        self.side_var = tk.StringVar(value='X')
        tk.Radiobutton(self.frame, text="Play as X", variable=self.side_var, value='X').pack(anchor='w')
        tk.Radiobutton(self.frame, text="Play as O", variable=self.side_var, value='O').pack(anchor='w')

        # Start Button
        tk.Button(self.frame, text="Start Game", font=('Helvetica', 12, 'bold'),
                  bg='#4CAF50', fg='white', command=self.start_game).pack(pady=20)

    def start_game(self):
        """Transitions from setup screen to the interactive board"""
        self.playerLetter = self.side_var.get()
        self.computerLetter = 'O' if self.playerLetter == 'X' else 'X'

        # Clear menu screen
        self.frame.destroy()

        # Create game layout frame
        self.game_frame = tk.Frame(self.root, bg='#222')
        self.game_frame.pack()

        # Map out the visual layout mimicking your numpad board scheme
        # Row 1: 7, 8, 9 | Row 2: 4, 5, 6 | Row 3: 1, 2, 3
        board_layout = [
            [7, 8, 9],
            [4, 5, 6],
            [1, 2, 3]
        ]

        for r_idx, row in enumerate(board_layout):
            for c_idx, num in enumerate(row):
                btn = tk.Button(self.game_frame, text='', font=('Helvetica', 24, 'bold'),
                                height=2, width=5, bg='#333', fg='white',
                                activebackground='#555', activeforeground='white',
                                command=lambda n=num: self.player_move(n))
                btn.grid(row=r_idx, column=c_idx, padx=5, pady=5)
                self.buttons[num] = btn

        # Randomly choose who goes first
        if random.randint(0, 1) == 0:
            messagebox.showinfo("First Turn", "The Computer goes first!")
            self.root.after(500, self.computer_move)
        else:
            messagebox.showinfo("First Turn", "You go first!")

    def player_move(self, position):
        """Triggered when a player clicks a board square"""
        if isSpaceFree(self.board, position):
            self.make_gui_move(self.playerLetter, position, '#2196F3')

            if self.check_game_over(self.playerLetter, "Congrats, you won!"):
                return

            # Disable interaction while computer is thinking
            self.toggle_buttons(state="disabled")
            self.root.after(400, self.computer_move)

    def computer_move(self):
        """Calculates AI action and visualizes it"""
        diff = self.difficulty.get()

        if diff == 1:
            move = getComputerMoveEasy(self.board)
        elif diff == 2:
            move = getComputerMoveMedium(self.board, self.computerLetter)
        else:
            move = getComputerMoveHard(self.board, self.computerLetter, self.playerLetter)

        if move:
            self.make_gui_move(self.computerLetter, move, '#f44336')
            self.toggle_buttons(state="normal")
            self.check_game_over(self.computerLetter, "The computer beat you!")

    def make_gui_move(self, letter, position, bg_color):
        """Updates internal structure array alongside external visual element"""
        MakeMove(self.board, letter, position)
        self.buttons[position].config(text=letter, bg=bg_color, state="disabled")

    def toggle_buttons(self, state):
        """Enables/Disables vacant board slots smoothly"""
        for pos, btn in self.buttons.items():
            if isSpaceFree(self.board, pos):
                btn.config(state=state)

    def check_game_over(self, letter, win_message):
        """Inspects structural states and serves outcome notifications"""
        if isWinner(self.board, letter):
            messagebox.showinfo("Game Over", win_message)
            self.prompt_restart()
            return True
        elif isBoardFull(self.board):
            messagebox.showinfo("Game Over", "It's a tie!")
            self.prompt_restart()
            return True
        return False

    def prompt_restart(self):
        """Offers a modern choice interface box to play again"""
        if messagebox.askyesno("Play Again?", "Would you like to play another match?"):
            self.game_frame.destroy()
            self.board = [' '] * 10
            self.buttons = {}
            self.setup_menu()
        else:
            self.root.quit()


# Run the app
if __name__ == "__main__":
    window = tk.Tk()
    app = TicTacToeGUI(window)
    window.mainloop()