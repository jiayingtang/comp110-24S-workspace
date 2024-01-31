"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730621008"

# Prompt for Player 1's secret location
secret_location = int(input("Pick a secret boat location between 1 and 4: "))
if secret_location < 1:
    print(f"Error! {secret_location} too low!")
    exit()
elif secret_location > 4:
    print(f"Error! {secret_location} too high!")
    exit()

# Prompt for Player 2's guess
guess = int(input("Guess a number between 1 and 4: "))
if guess < 1:
    print(f"Error! {guess} too low!")
    exit()
elif guess > 4:
    print(f"Error! {guess} too high!")
    exit()

# Check if the guess is correct 
if guess == secret_location:
    print("Correct! You hit the ship.")
    hit = True
else:
    print("Incorrect! You missed the ship.")
    hit = False

# Define box colors
BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"

# Build the result 
result = ""
if guess == 1:
    box = RED_BOX if hit else WHITE_BOX
    result = box + BLUE_BOX + BLUE_BOX + BLUE_BOX
elif guess == 2:
    box = RED_BOX if hit else WHITE_BOX
    result = BLUE_BOX + box + BLUE_BOX + BLUE_BOX
elif guess == 3:
    box = RED_BOX if hit else WHITE_BOX
    result = BLUE_BOX + BLUE_BOX + box + BLUE_BOX
elif guess == 4:
    box = RED_BOX if hit else WHITE_BOX
    result = BLUE_BOX + BLUE_BOX + BLUE_BOX + box

# Print the result
print(result)
