# Write a program using functions and return statement to check whether a number is even or odd

from cgi import print_directory


def is_even(a):
    if a % 2 == 0:
        return 1

    else:
        return 0

num= eval(input('Enter the number: '))
flag= is_even(num)

if flag == 1:
    print(f'{num} is an even number')

else:
    print(f'{num} is an odd number')







