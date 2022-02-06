# Write a program that finds the sum of all the numbers in a list
# using a while loop

from itertools import count


print('--- A Program to print the sum of natural numbers ---')
print()

list_= [1,2,3,4,5,6,7,8,9,10]
counter= len(list_)
while counter > 0:
    sum= 0
    for item in list_:
        sum += item
        counter -= 1
    break

print(f'The sum is {sum}')

print()