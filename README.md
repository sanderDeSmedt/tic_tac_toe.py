# Tic Tac Toe
A Python implementation of the classic Tic Tac Toe game with three difficulty levels, featuring AI opponents ranging from random moves to an unbeatable minimax algorithm.
Features

## Three Difficulty Levels

Easy: Computer makes random moves
Medium: Strategic AI that tries to win, blocks your moves, and follows tactical patterns
Hard: Unbeatable AI using the minimax algorithm


Player Choice: Choose to play as X or O
Random Turn Order: Either you or the computer can go first
Clean Board Display: Clear visual representation of the game board
Replay Option: Play multiple games without restarting the program

## How to Play

Run the program:

    python3 tictactoe.py

Choose whether you want to be X or O
Select your difficulty level:

- 1 for Easy
- 2 for Medium
- 3 for Hard


The game will randomly decide who goes first
Enter your move by typing a number from 1-9 corresponding to the board position:

    7 | 8 | 9
   ----------
    4 | 5 | 6
   ----------
    1 | 2 | 3

Try to get three in a row (horizontally, vertically, or diagonally) before the computer does!

## Difficulty Breakdown
Easy Mode
The computer selects moves completely at random from available spaces. Great for beginners or young players who want a fair chance to win.
Medium Mode
The computer uses strategic thinking:

Takes winning moves when available
Blocks your winning moves
Prefers the center position
Takes corners over side positions
Provides a good challenge for intermediate players

Hard Mode
The computer uses the minimax algorithm to evaluate all possible future game states. It plays perfectly and cannot be beaten - you can only hope for a tie. Perfect for experienced players who want the ultimate challenge.

## equirements

Python 3.x
No external libraries required (uses only standard Python libraries)

## Game Rules

Players alternate turns placing their mark (X or O) on the board
The first player to get three marks in a row (horizontally, vertically, or diagonally) wins
If all 9 squares are filled without a winner, the game is a tie
Players cannot place their mark on an occupied square
