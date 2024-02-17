"""EX02 - One Shot Battleship."""

__author__ = "730621008"

# Define grid size, secret row, and secret column
g_size = 4
s_row = 3
s_column = 2


def get_guess(prompt: str) -> int:
    """Prompt the user for a guess and ensure it's within the grid bounds."""
    while True:
        guess = int(input(prompt))
        if 1 <= guess <= g_size:
            return guess
        print(f"The grid is only {g_size} by {g_size}. Try again: ", end="")


def print_grid(row_guess: int, column_guess: int) -> None:
    """Prints the game grid, marking the guess location with appropriate box color."""
    for row in range(1, g_size + 1):
        for column in range(1, g_size + 1):
            if row == s_row and column == s_column and row == row_guess and column == column_guess:
                print(RED_BOX, end="")
            elif row == row_guess and column == column_guess:
                print(WHITE_BOX, end="")
            else:
                print(BLUE_BOX, end="")
        print()  # Newline after each row


# Constants for box types
BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"

# Prompt user for row and column guesses
r_guess = get_guess("Guess a row: ")
c_guess = get_guess("Guess a column: ")


# Print the grid with the guess result
print_grid(r_guess, c_guess)


# Print feedback with hints
if r_guess == s_row and c_guess == s_column:
    print("Hit!")
elif r_guess == s_row:
    print("Close! Correct row, wrong column.")
elif c_guess == s_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")
