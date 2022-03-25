# Write a program that prints the maximum and the minimum value in a dictionary

print('----- A program to print maximum and minimum value-----')
print()

import functools
def max_ele(x,y):
    return x>y
def min_ele(x,y):
    x<y
    return x<y
num_list = {4,1,8,6,9,20}

print(f'The maximum value in the dictionary is : {functools.reduce(max, num_list)}')
print(f'The minimum value in the dictionary is : {functools.reduce(min, num_list)}')
