# How would you modify the program in 3 above, so that the
# program tells the user if there guess is too high or too low, each time they
# guess. HINT: put an if statement inside the while loop.

# Author: Rodrigo De Martino Ucedo

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("Too low")