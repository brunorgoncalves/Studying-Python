text = input("Type a text: ")
VOWELS = "AEIOU"

for letter in text:
    if letter.upper() in VOWELS:
        print(letter, end="")
else:
    print() # Add a line break


for number in range(0, 91, 9):
    print (number, end="")