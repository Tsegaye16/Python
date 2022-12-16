import string
import random


print("Welcome to simple Password Generator tool developed by group 4 members!")
print("our simple app let you create password that cannot be guessed and cracked")
print("******************************************")
print("*Please Select from the following options*")
print("******************************************\n")
print("1: To start password generator tool: ")
print("2: to exit the program")


def startgenerator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    number_of_letters = int(input("How many LETTERS would you like in your password: "))
    number_of_symbols = int(input("How many SYMBOLS would you like in your password: "))
    number_of_digits = int(input("How many DIGITS would you like in your password: "))

    def selector(array, number):
        chosen = ''
        for counter in range(number):
            chosen += ''.join(random.choice(array))

        return chosen

    chosenLetters = selector(letters, number_of_letters)
    chosenSymbols = selector(symbols, number_of_symbols)
    chosenNumbers = selector(numbers, number_of_digits)

    print("Selected letters are: ", chosenLetters)
    print("Selected Symbols are: ", chosenSymbols)
    print("Selected Digits are: ", chosenNumbers)

    alphabet = chosenLetters + chosenSymbols + chosenNumbers

    finalPassword = alphabet

    pass_length = number_of_letters + number_of_symbols + number_of_digits

    # for i in range(pass_length):
    #     finalPassword += ''.join(random.choice(alphabet))

    print("Your Generated Combination of password from the alphabet is: ", finalPassword)
    print("Length of your Password is: ", pass_length)

    if pass_length < 8:
        print("Your password length must be greater than 8 characters ❌")
    if pass_length >= 8 and pass_length < 12:
        print("Your password strength is GOOD ✔️")
    if pass_length >= 12:
        print("Your password Strength is GREAT ✔️✔️")


option = int(input("Please Enter your option: "))

if option == 1:
    startgenerator()
if option == 2:
  exit(1)
