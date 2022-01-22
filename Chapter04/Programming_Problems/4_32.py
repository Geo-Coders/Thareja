# Write a program to print a table of sine and cos functions for the interval from 0-360 degrees in increment of 15
print('----- A program to print a table of sine and cos -----')
print()
from cmath import cos, sin
import math


math
print('\tsine    \t\tcos')
print('---------------------------------------------')
for i in range(0, 361, 15):
    print(sin(i), cos(i))
    print()
