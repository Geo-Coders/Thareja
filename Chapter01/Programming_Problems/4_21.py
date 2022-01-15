# Writing a program to test if a given number is a power of 2.

print('--- A Program to test powers of 2 ---')

print()

num = int(input('Enter a value to test: '))

if (num != 0) and (num & (num - 1 ) == 0):
    print('\nThe number is a power of 2')
else:
    print('The number is not a Power of 2')