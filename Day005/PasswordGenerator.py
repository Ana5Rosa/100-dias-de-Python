import random

print("Welcome to the PyPassword Generator!")
qtt_letters = int(input("How many letters would you like in your password? "))
qtt_symbols = int(input("How many symbols would you like in your password? "))
qtt_numbers = int(input("How many numbers would you like in your password? "))

listOfLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
listOfNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
listOfSymbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

listPassword = []
for letter in range(0, qtt_letters):
    char = random.choice(listOfLetters)
    listPassword.append(char)

for number in range(0, qtt_numbers):
    char = random.choice(listOfNumbers)
    j = random.randint(0, len(listPassword) - 1)
    listPassword.insert(j, char)

for symbol in range(0, qtt_symbols):
    char = random.choice(listOfSymbols)
    j = random.randint(0, len(listPassword) - 1)
    listPassword.insert(j, char)

password = ""
for caracter in listPassword:
    password += caracter

print(f"Here is your password: {password}")
    

