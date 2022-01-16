# Write a program that prints absolute value, square root, and cube of a number.

import math

def cube(x):
    return x**3

a= -100
print(f'a = {a}')

a= abs(a)

print(f'abs(a) = {a}')
print(f'Square root of {a} = {math.sqrt(a)}')
print(f'Cube of {a} = {cube(a)}')

