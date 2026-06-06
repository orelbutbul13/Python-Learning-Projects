# Passphrase Checker
# Keeps asking the user to enter the correct passphrase
# until they type it correctly.

passphrase = "sillygoose"

user_input = input('Enter the word "sillygoose": ').lower()

while user_input != passphrase:
    print('You need to enter the word "sillygoose".')
    user_input = input('Enter the word "sillygoose": ').lower()

print("WOOHOO! That is teamwork.")
