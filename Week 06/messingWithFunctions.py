# Messing with functions
# to demonstrate the defining and using functions.

# Author: Rodrigo De Martino Ucedo

#x, y, z = (1, 2, 3)
#print (x, y, z, sep="", end="")
#print (f"{x}-{y} {z}")
#print ("{} {}--{}".format(x, y, z))

def topower(number, power =3):
    #print(number)
    return (number ** power)

#ans = cube(2)
#print (f"We got {ans}")
num = 45
print (f"and {num} is {topower(num)}")