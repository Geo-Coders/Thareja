# Write a program that prompts the user to enter a number
# If the number is positive or xero print it, otherwise raise an exception

try:
    num = int(input('Enter a number :'))
    if num >= 0:
        print(num)
    else:
        raise ValueError('Negative number not allowed')
except ValueError as e:
    print(e)