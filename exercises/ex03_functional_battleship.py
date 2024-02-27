"""EX03 functional battleship."""

__author__ = "730621008"


import random


def input_guess(size: int, spec: str) -> int:
    """Prompts the user for a guess of a row or column within the bounds of the grid size."""
    assert spec == "row" or spec == "column"
    while True:
        guess = input(f"Guess a {spec}: ")
        # Attempt to convert the guess to an integer and validate its range
        try:
            guess = int(guess)
            if 1 <= guess <= size:
                return guess
            else:
                print(f"The grid is only {size} by {size}. Try again:")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def print_grid(size: int, guess_row: int, guess_col: int, is_correct: bool) -> None:
    """Prints the game grid based on the user's guess and whether it was correct."""
    WHITE_BOX = "⬜"
    RED_BOX = "🟥"
    BLUE_BOX = "🟦"
    
    for row in range(1, size + 1):
        for col in range(1, size + 1):
            if row == guess_row and col == guess_col:
                print(RED_BOX if is_correct else WHITE_BOX, end="")
            else:
                print(BLUE_BOX, end="")
        print()  # Move to the next line after printing one row.


def correct_guess(secret_row: int, secret_col: int, guess_row: int, guess_col: int) -> bool:
    """Determines if the user's guess matches the secret location of the boat."""
    return secret_row == guess_row and secret_col == guess_col


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """The main game loop for Battleship."""
    max_turns = 5
    correct = False
    
    for turn in range(1, max_turns + 1):
        print(f"=== Turn {turn}/{max_turns} ===")
        
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        
        if correct_guess(secret_row, secret_column, row_guess, column_guess):
            print(f"Hit! You won in {turn}/{max_turns} turns!")
            correct = True
            break
        else:
            print("Miss!")
            print_grid(grid_size, row_guess, column_guess, False)
    
    if not correct:
        print(f"{max_turns}/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))