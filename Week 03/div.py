# Program that reads in two number and
# output the integer answer and remainder

# Author: Rodrigo De Martino Ucedo

x = int(input("Enter first nmber: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x // y) # // give the int division
remainder = x % y # % gives the remainder

print ("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))
