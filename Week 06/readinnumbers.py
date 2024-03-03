# Read in two numbers and multiple them
# Author: Rodrigo De Martino Ucedo

def readNum(message = "enter a number:"):
    num = False
    while (not num):
        try:
            num  = int(input(message))
        except ValueError:
            print ("That was not a number ", end="")
    return num    

num1 = readNum()
num2 = readNum("Enter another number:")

answer = num1 * num2

print(f"Answer is {answer}")