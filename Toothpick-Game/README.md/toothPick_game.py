# Toothpick Game

print("Welcome to the Toothpick Game!")
print("*" * 30)
print("The rules are simple:")
print("1. There are 21 toothpicks on the table.")
print("2. Players will take turns picking 1 to 3 toothpicks.")
print("3. The player who picks the last toothpick wins!")

# Get player names
player1Name = input("Enter Player 1 name: ")
player2Name = input("Enter Player 2 name: ")

# Starting number of toothpicks
toothpicks = 21

# Main game loop
while True:
    # Show current toothpicks
    print()
    print('|' * toothpicks)
    print(f'There are {toothpicks} toothpicks left')

    # Player 1 turn
    while True:
        player1Choice = int(input(f'{player1Name}, how many toothpicks do you take? '))

        if 1 <= player1Choice <= 3 and player1Choice <= toothpicks:
            break

        print(f'Invalid choice. Choose 1 to 3, and no more than {toothpicks}.')

    toothpicks -= player1Choice

    # Check if Player 1 won
    if toothpicks <= 0:
        print(f'{player1Name} wins the game!')
        break

    # Show current toothpicks
    print()
    print('|' * toothpicks)
    print(f'There are {toothpicks} toothpicks left')

    # Player 2 turn
    while True:
        player2Choice = int(input(f'{player2Name}, how many toothpicks do you take? '))

        if 1 <= player2Choice <= 3 and player2Choice <= toothpicks:
            break

        print(f'Invalid choice. Choose 1 to 3, and no more than {toothpicks}.')

    toothpicks -= player2Choice

    # Check if Player 2 won
    if toothpicks <= 0:
        print(f'{player2Name} wins the game!')
        break

print('GAME OVER!!!')
