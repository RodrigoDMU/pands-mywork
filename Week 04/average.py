# This program reads in numbers until
# the user enters )
# it will them print back out again
# and their average

# Author: Rodrigo De Martino Ucedo

numbers = []

#First number then we check if it is 0 in the while loop
number = int(input("Enter number (0 to quit):"))

while number != 0:
    numbers.append(number)

    # read the next number and check if )
    number = int(input("Enter another (0 to quit):"))

for value in numbers:
    print (value)

# I want average to be a float   
average = float(sum(numbers)) / len(numbers)
print(f"The average is {average}")