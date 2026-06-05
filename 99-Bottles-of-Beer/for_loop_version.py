for numberOfBottles in range(99, 0, -1):

    if numberOfBottles == 1:
        print(f'{numberOfBottles} bottle of beer on the wall.')
        print(f'{numberOfBottles} bottle of beer.')
        print('Take one down, pass it around, no more bottles of beer on the wall.')
    elif numberOfBottles == 2:
        print(f'{numberOfBottles} bottles of beer on the wall.')
        print(f'{numberOfBottles} bottles of beer.')
        print('Take one down, pass it around, 1 bottle of beer on the wall.')
    else:
        print(f'{numberOfBottles} bottles of beer on the wall.')
        print(f'{numberOfBottles} bottles of beer.')
        print(f'Take one down, pass it around, {numberOfBottles - 1} bottles of beer on the wall.')

    print('*' * 50)
