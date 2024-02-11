# This program prints out a random fruit

import random

fruits1 = ['Apple', 'Orange', 'Banana', 'Pear'] # list is square brackets []

# We want a random number between ) 0 and lenght -1
index = random.randint (0,len(fruits1)-1)

fruit1 = fruits1[index]
print ("A random Fruit: {}".format(fruit1))

fruits2 = ('Apple', 'Orange', 'Banana', 'Pear') # tuple is round bracktes ()

# We want a random number between ) 0 and lenght -1
index = random.randint (0,len(fruits2)-1)

fruit2 = fruits2[index]
print ("A random Fruit: {}".format(fruit2))