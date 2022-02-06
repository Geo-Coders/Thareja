# Write a program that uses map() to print the double 
# value of each element in a list.

print('--- A Program to double value in a list ---')
print()

def func(x):
    return (lambda x: x*x)(x)


func_= map(func,[1,2,3,4,5,6,7,8,9,10])

print('The Original list : ')
print('[1,2,3,4,5,6,7,8,9,10]')
print()

print('The Double list : ')
print(list(func_))
print()
