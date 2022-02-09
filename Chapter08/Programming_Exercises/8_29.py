# Write a program that counts the number of times a value appears in the list.
# Use a loop to do the same.

print('--- A Program to count the number of times a value appears in a list ---')
print()

def countX(list_, x):
    count = 0
    for ele in list_:
        if (ele == x):
            count += 1
    return count

x = int(input('Enter a number : '))
list_= [1,2,3,4,5,3,2,2,5,6,5,6,7,7,8,8,9,0,0,6,6,55,44,3]
print()
print('{} has occurred {} times'.format(x, countX(list_, x)))
