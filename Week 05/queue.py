# Create a program that puts 10 random numbers into a queue(list),
# the program should then output all the values in the queue,
# then take the numbers from the queue one at a time, print it 
# and the current numbers still in the queue. 
# (the command pop(0) takes the first element out of a list)

# Author: Rodrigo De Martino Ucedo

import random
queue = []
numberOfNumber = 10
rangeTo = 100

for n in range(0, numberOfNumber):
    queue.append(random.randint(0, rangeTo))

print (f"Queue is {queue}")

while len(queue) != 0:

    currentNumber = queue.pop(0)
    print (f"Current number os {currentNumber} and the queue is {queue}")

print ("The queue is now emprty")