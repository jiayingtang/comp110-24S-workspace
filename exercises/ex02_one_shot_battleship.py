"""EX02 - One Shot Battleship."""

__author__ = "730621008"

# Define constants for grid size, secret row, and secret column
GRID_SIZE = 4
SECRET_ROW = 3
SECRET_COLUMN = 2

# Function to get user guess within grid bounds
def get_guess(prompt):
    while True:
        guess = int(input(prompt))
        if 1 <= guess <= GRID_SIZE:
            return guess
        print(f"The grid is only {GRID_SIZE} by {GRID_SIZE}. Try again: ", end="")

# Prompt user for row and column guesses
row_guess = get_guess("Guess a row: ")
column_guess = get_guess("Guess a column: ")

# Determine if the guess is a hit or miss
if row_guess == SECRET_ROW and column_guess == SECRET_COLUMN:
    print("Hit!")
else:
    print("Miss!")
# Constants for box types
BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"

# Function to print the game grid
def print_grid(row_guess, column_guess):
    for row in range(1, GRID_SIZE + 1):
        for column in range(1, GRID_SIZE + 1):
            if row == SECRET_ROW and column == SECRET_COLUMN and row == row_guess and column == column_guess:
                print(RED_BOX, end="")
            elif row == row_guess and column == column_guess:
                print(WHITE_BOX, end="")
            else:
                print(BLUE_BOX, end="")
        print()  # Newline after each row

# Print the grid with the guess result
print_grid(row_guess, column_guess)
# Updated feedback with hints
if row_guess == SECRET_ROW and column_guess == SECRET_COLUMN:
    print("Hit!")
elif row_guess == SECRET_ROW:
    print("Close! Correct row, wrong column.")
elif column_guess == SECRET_COLUMN:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")
