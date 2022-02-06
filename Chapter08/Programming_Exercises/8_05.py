# Write a Program using reduce() function to calculate the 
# sum of first 10 natural numbers.

from functools import reduce

print('--- A Program to print the first 10 natural numbers ---')
print()

def added(x,y):
    return (lambda x,y: x+y)(x,y)

added_no= reduce(added, [1,2,3,4,5,6,7,8,9,10])

print(f'The sum of the first natural numbers is : {added_no}')

print()
