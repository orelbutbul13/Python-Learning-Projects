# Loop Through a Word
# Demonstrates how to iterate through each character in a string
# using both a for loop and a while loop.

word = "supercalifragilisticexpialidocious"

# For loop version
for character in word:
    print(character)

print("-" * 50)

# While loop version
index = 0

while index < len(word):
    print(word[index])
    index += 1
