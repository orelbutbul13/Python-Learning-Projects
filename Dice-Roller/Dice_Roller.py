# Dice Roller
# Interactive dice rolling simulator.
# Allows the user to choose how many dice to roll and how many sides each die has.

from random import randint

# Get dice settings from the user
num_of_dice = int(input("How many dice are you rolling? "))
num_sides = int(input("How many sides on each die? "))

while True:
    # Store all dice rolls in one string
    result = "|"

    # Roll each die and add the result to the output string
    for die in range(num_of_dice):
        roll = randint(1, num_sides)
        result += f"{roll}|"

    # Print the full roll result once
    print(result)

    # Ask the user if they want to roll again
    reply = input("Roll again? (q to quit): ").lower()

    if reply == "q":
        print("Game over")
        break
