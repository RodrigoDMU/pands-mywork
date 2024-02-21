# Write a program (guess1.py) that prompts the user to guess a number, the
# program should keep prompting the user to guess the number until the user
# gets the right on

# Author: Rodrigo De Martino Ucedo


numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess the number: "))

print ("Well done! Yes the number was", numberToGuess)