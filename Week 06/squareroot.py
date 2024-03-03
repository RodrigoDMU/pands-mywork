# Write a program that takes a positive floating-point number as 
# input and outputs an approximation of its square root.

# You should create a function called <tt>sqrt</tt> that does this.

# I am asking you to create your own sqrt function and not 
# to use the built in functions x ** .5 or math.sqrt(x).

# This is to demonstrate that you can research and code a 
# process (If you really needed the square root you would use 
# one of the above methods). I suggest that you look at the newton
# method at estimating square roots. 

# This is a more difficult task than some of the others, 
# but will be marked equally, so only do as much work on 
# this as you feel comfortable.

# Author: Rodrigo De Martino Ucedo


x = float(input("Please enter a positive number: "))
a = 2
while abs(x - (a * a)) > 0.00001: 
    p = (a + (x / a)) / 2
    a = p
print(f"The square root of {x} is approx {p:.1f}.")


# Reference: Introdução á Programação com PythonÇ Algoritmos 
# e Lógica de Programação para Iniciantes

# Using import math
import math

x = float(input("Please enter a positive number: "))
sqrRoot = math.sqrt(x)

print (f"The square root of {x} is approx. {sqrRoot:.1f}.")

   