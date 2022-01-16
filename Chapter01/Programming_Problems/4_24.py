# Write a program to display the sin(x) value 
# where x ranges from 0 to 360 in steps of 15

from cmath import sin
import math


for i in range(0, 361, 15):
    print(sin (i), end = ' ')
    