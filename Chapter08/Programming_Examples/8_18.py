# Write a program to find largest value in a list using reduce() function
import functools
def max_ele(x,y):
    return x>y
num_list = [4,1,8,2,9,3,0]
print(f'Largest value in the list is :  {functools.reduce(max,num_list)}')