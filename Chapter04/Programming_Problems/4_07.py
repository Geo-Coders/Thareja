# Write a program to demonstrate the use of nested if structure
print('--- A Program to demonstrate the use of nested if structure ---')
print()
print('Enter -1 to quit at any time')

num= int(input('Enter a Number to determine whether positive, negative or zero: '))
while num != -1:
    if num >= 0:
        if num == 0:
            print("Zero")
        else:
            print("Positive number")
    else:
        print("Negative number")

    num= int(input('Enter another number: '))