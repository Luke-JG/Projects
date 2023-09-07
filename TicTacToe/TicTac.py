import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main game window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Define player symbols
PLAYER_X = "X"
PLAYER_O = "O"

# Define difficulty levels
DIFFICULTY_EASY = 1
DIFFICULTY_MEDIUM = 2
DIFFICULTY_HARD = 3

# Define ASCII art for game events
ASCII_WIN = """
  _____ _     _  ____  _      ____  _     
 |_   _| |__ (_)|  _ \| | __ |  _ \| |    
   | | | '_ \| || | | | |/ / | |_) | |    
   | | | | | | || |_| |   <  |  __/| |___ 
   |_| |_| |_|_||____/|_|\_\ |_|   |_____|
"""

ASCII_DRAW = """
  ____ ____ _  ___ ____ ____ ____ ____  
  | __ |  | |   |  |__/ |___ |    |__/  
  |__| |__| |   |  |  \ |___ |___ |  \  
"""

ASCII_LOSE = """
  __   _ ____ ____ _  _ ____ _  _ ____  
  | \_/  |___ |___ |\ | |  | |\ | | __  
  |  |   |___ |    | \| |__| | \| |__] 
"""

# Update the ASCII art for game events


# Initialize the game board
board = [" " for _ in range(9)]

# Initialize difficulty level
current_difficulty = DIFFICULTY_MEDIUM

# Initialize player turn
current_player = PLAYER_X

# Check if the game is over
game_over = False

# Create GUI buttons
buttons = [tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2, command=lambda i=i: make_move(i))
           for i in range(9)]

# Place buttons on the grid
for row in range(3):
    for col in range(3):
        buttons[row * 3 + col].grid(row=row, column=col)

# Create difficulty level radio buttons
difficulty_var = tk.IntVar()

easy_button = tk.Radiobutton(root, text="Easy", variable=difficulty_var, value=DIFFICULTY_EASY)
medium_button = tk.Radiobutton(root, text="Medium", variable=difficulty_var, value=DIFFICULTY_MEDIUM)
hard_button = tk.Radiobutton(root, text="Hard", variable=difficulty_var, value=DIFFICULTY_HARD)

easy_button.grid(row=3, column=0)
medium_button.grid(row=3, column=1)
hard_button.grid(row=3, column=2)

# Initialize the game
def start_game():
    global board, current_player, game_over
    board = [" " for _ in range(9)]
    current_player = PLAYER_X
    game_over = False
    update_board()

# Make a move (player or AI)
def make_move(index):
    global current_player, game_over

    if not game_over and board[index] == " ":
        board[index] = current_player
        update_board()
        check_winner(current_player)
        if not game_over:
            if current_player == PLAYER_X:
                current_player = PLAYER_O
            else:
                current_player = PLAYER_X
            if current_player == PLAYER_O:
                ai_move()

# Update the GUI board
def update_board():
    for i in range(9):
        buttons[i].config(text=board[i])
    check_draw()

# Check for a winner
def check_winner(player):
    global game_over
    for combo in WINNING_COMBOS:
        if all(board[i] == player for i in combo):
            game_over = True
            display_winner(player)
            return

# Check for a draw
def check_draw():
    global game_over
    if " " not in board:
        game_over = True
        display_draw()

# Display the winner
def display_winner(player):
    winner_label = tk.Label(root, text=f"Player {player} wins!", font=("Arial", 16))
    winner_label.grid(row=4, column=0, columnspan=3)
    show_ascii_art(ASCII_WIN)

# Display a draw
def display_draw():
    draw_label = tk.Label(root, text="It's a draw!", font=("Arial", 16))
    draw_label.grid(row=4, column=0, columnspan=3)
    show_ascii_art(ASCII_DRAW)

# Display the loser
def display_loser(player):
    loser_label = tk.Label(root, text=f"Player {player} loses!", font=("Arial", 16))
    loser_label.grid(row=4, column=0, columnspan=3)
    show_ascii_art(ASCII_LOSE)

# Show ASCII art
def show_ascii_art(ascii_art):
    ascii_label = tk.Label(root, text=ascii_art, font=("Courier New", 16))
    ascii_label.grid(row=5, column=0, columnspan=3)

# AI opponent (Minimax algorithm)
def ai_move():
    global current_player
    if current_player == PLAYER_O:
        difficulty = difficulty_var.get()
        if difficulty == DIFFICULTY_EASY:
            make_random_move()
        elif difficulty == DIFFICULTY_MEDIUM:
            make_optimal_move_medium()
        elif difficulty == DIFFICULTY_HARD:
            make_optimal_move_hard()

# Make a random move for AI (Easy difficulty)
def make_random_move():
    empty_cells = [i for i in range(9) if board[i] == " "]
    if empty_cells:
        ai_choice = random.choice(empty_cells)
        make_move(ai_choice)

# Make an optimal move for AI (Medium difficulty)
def make_optimal_move_medium():
    empty_cells = [i for i in range(9) if board[i] == " "]
    if empty_cells:
        ai_choice = random.choice(empty_cells)
        make_move(ai_choice)

# Make an optimal move for AI (Hard difficulty using Minimax)
def make_optimal_move_hard():
    best_score = float("-inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = PLAYER_O
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        make_move(best_move)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(PLAYER_X):
        return -1
    elif check_winner(PLAYER_O):
        return 1
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = PLAYER_O
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score

    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = PLAYER_X
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    # Minimax algorithm logic here
    pass

# Define winning combinations
WINNING_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]  # Diagonals
]

# Initialize score counters
score_x = 0
score_o = 0

# Create a label to display the scores
score_label = tk.Label(root, text=f"Player X: {score_x} | Player O: {score_o}", font=("Arial", 16))
score_label.grid(row=6, column=0, columnspan=3)

# Function to update the score label
def update_score_label():
    score_label.config(text=f"Player X: {score_x} | Player O: {score_o}")

# Reset the scores and the game board
def reset_game():
    global board, current_player, game_over
    board = [" " for _ in range(9)]
    current_player = PLAYER_X
    game_over = False
    update_board()
    update_score_label()  # Reset the score label
    for btn in buttons:
        btn.config(state="normal")  # Re-enable the buttons

# Create a Reset Game button
reset_button = tk.Button(root, text="Reset Game", font=("Arial", 16), command=reset_game)
reset_button.grid(row=7, column=0, columnspan=3)

# Modify the display_winner, display_draw, and display_loser functions to update the scores
def display_winner(player):
    global score_x, score_o
    if player == PLAYER_X:
        score_x += 1
    else:
        score_o += 1
    update_score_label()
    winner_label = tk.Label(root, text=f"Player {player} wins!", font=("Arial", 16))
    winner_label.grid(row=4, column=0, columnspan=3)
    show_ascii_art(ASCII_WIN)

def display_draw():
    global score_x, score_o
    score_x += 0.5
    score_o += 0.5
    update_score_label()
    draw_label = tk.Label(root, text="It's a draw!", font=("Arial", 16))
    draw_label.grid(row=4, column=0, columnspan=3)
    show_ascii_art(ASCII_DRAW)

def display_loser(player):
    global score_x, score_o
    if player == PLAYER_X:
        score_o += 1
    else:
        score_x += 1
    update_score_label()
    loser_label = tk.Label(root, text=f"Player {player} loses!", font=("Arial", 16))
    loser_label.grid(row=4, column=0, columnspan=3)
    show_ascii_art(ASCII_LOSE)

# Update the AI move function to disable buttons when the game is over
def ai_move():
    global current_player
    if current_player == PLAYER_O and not game_over:
        difficulty = difficulty_var.get()
        if difficulty == DIFFICULTY_EASY:
            make_random_move()
        elif difficulty == DIFFICULTY_MEDIUM:
            make_optimal_move_medium()
        elif difficulty == DIFFICULTY_HARD:
            make_optimal_move_hard()

# Update the make_move function to disable buttons when the game is over
def make_move(index):
    global current_player, game_over
    if not game_over and board[index] == " ":
        board[index] = current_player
        update_board()
        check_winner(current_player)
        if not game_over:
            if current_player == PLAYER_X:
                current_player = PLAYER_O
            else:
                current_player = PLAYER_X
            if current_player == PLAYER_O:
                ai_move()
        else:
            for btn in buttons:
                btn.config(state="disabled")  # Disable buttons when the game is over

# Start the game
start_game()

# Run the GUI main loop
root.mainloop()

