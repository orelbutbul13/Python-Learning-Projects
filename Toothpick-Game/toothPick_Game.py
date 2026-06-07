# Toothpick Game

print("Welcome to the Toothpick Game!")
print("*" * 30)
print("The rules are simple:")
print("1. There are 21 toothpicks on the table.")
print("2. Players take turns picking 1 to 3 toothpicks.")
print("3. The player who picks the last toothpick wins!")

player1Name = input("Enter Player 1 name: ")
player2Name = input("Enter Player 2 name: ")

toothpicks = 21

while True:

    print()
    print('|' * toothpicks)
    print(f'There are {toothpicks} toothpicks left')

    # Player 1 Turn
    player1Choice = int(input(f'{player1Name}, how many toothpicks do you take? '))

    while player1Choice not in (1, 2, 3):
        player1Choice = int(input(f'{player1Name}, you can only choose 1, 2, or 3: '))

    toothpicks -= player1Choice

    if toothpicks <= 0:
        print(f'{player1Name} wins the game!')
        break

    print()
    print('|' * toothpicks)
    print(f'There are {toothpicks} toothpicks left')

    # Player 2 Turn
    player2Choice = int(input(f'{player2Name}, how many toothpicks do you take? '))

    while player2Choice not in (1, 2, 3):
        player2Choice = int(input(f'{player2Name}, you can only choose 1, 2, or 3: '))

    toothpicks -= player2Choice

    if toothpicks <= 0:
        print(f'{player2Name} wins the game!')
        break

print("GAME OVER!!!")
