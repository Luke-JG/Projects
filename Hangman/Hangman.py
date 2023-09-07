import tkinter as tk
from tkinter import messagebox
import random

# Define word categories
word_categories = {
    "Fruits": ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"],
    "Animals": ["cat", "dog", "elephant", "giraffe", "kangaroo", "lion", "tiger"],
    "Countries": ["argentina", "brazil", "canada", "denmark", "egypt", "france", "germany"],
}

# Initialize variables
selected_category = ""
word_to_guess = ""
attempts = 6
guessed_letters = set()
display_word = []

# ASCII art for hangman animations
hangman_animations = [
    """
       -----
       |   |
           |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    """,
]

# Initialize the game
def start_game():
    global selected_category, word_to_guess, attempts, guessed_letters, display_word
    selected_category = category_var.get()
    word_to_guess = random.choice(word_categories[selected_category])
    attempts = 6
    guessed_letters = set()
    display_word = ["_"] * len(word_to_guess)
    update_display()
# Update the display with the current game state
def update_display():
    word_display.config(text=" ".join(display_word))
    attempts_display.config(text=f"Attempts left: {attempts}")
    guessed_display.config(text=f"Guessed letters: {' '.join(guessed_letters)}")
    guess_entry.delete(0, tk.END)
    update_hangman_image()
    score_display.config(text=f"Score: {score_var.get()}")

# Handle a guessed letter
# Handle a guessed letter
def guess_letter():
    global attempts
    letter = guess_entry.get().lower()
    if len(letter) != 1 or not letter.isalpha():
        messagebox.showerror("Invalid Input", "Please enter a single letter.")
        return
    if letter in guessed_letters:
        messagebox.showinfo("Already Guessed", f"You already guessed '{letter}'.")
        return
    guessed_letters.add(letter)
    if letter not in word_to_guess:
        attempts -= 1
    else:
        # Update the display_word to reflect correctly guessed letters
        for i, char in enumerate(word_to_guess):
            if char == letter:
                display_word[i] = letter
    update_display()
    if "_" not in display_word:
        messagebox.showinfo("You Win!", "Congratulations, you guessed the word!")
        # Increment the score when the player wins
        score_var.set(score_var.get() + 1)
        start_game()
    elif attempts == 0:
        messagebox.showinfo("Game Over", f"You're out of attempts. The word was '{word_to_guess}'.")
        start_game()


# Update the display with the current game state
def update_display():
    word_display.config(text=" ".join(display_word))
    attempts_display.config(text=f"Attempts left: {attempts}")
    guessed_display.config(text=f"Guessed letters: {' '.join(guessed_letters)}")
    guess_entry.delete(0, tk.END)
    update_hangman_image()

# Update the hangman image based on the number of attempts left
def update_hangman_image():
    hangman_frame.config(text=hangman_animations[6 - attempts])

# Create the main window
root = tk.Tk()
root.title("Hangman Game")

# Create a variable to hold the selected category
category_var = tk.StringVar()
category_var.set("Fruits")  # Default category
# Create a variable to hold the player's score
score_var = tk.IntVar()
score_var.set(0)  # Initial score

# Create and configure a label to display the player's score
score_display = tk.Label(root, text="Score: 0", font=("Arial", 16))
score_display.pack()

# Create and configure GUI elements
word_display = tk.Label(root, text="", font=("Arial", 24))
attempts_display = tk.Label(root, text="", font=("Arial", 16))
guessed_display = tk.Label(root, text="", font=("Arial", 16))
guess_entry = tk.Entry(root, font=("Arial", 16))
guess_button = tk.Button(root, text="Guess", command=guess_letter)
start_button = tk.Button(root, text="Start New Game", command=start_game)

# Create a dropdown menu for word categories
category_menu = tk.OptionMenu(root, category_var, *word_categories.keys())

# Hangman frame with ASCII art
hangman_frame = tk.Label(root, text="", font=("Courier New", 16), justify="left")
hangman_frame.config(width=40, height=15)

# Arrange GUI elements on the screen
word_display.pack()
attempts_display.pack()
guessed_display.pack()
category_menu.pack()
guess_entry.pack()
guess_button.pack()
start_button.pack()
hangman_frame.pack()

# Start the game
start_game()

# Run the GUI main loop
root.mainloop()
