# Write a function that displays 'Hello name', for any given name passed to it.

print('\t\t--- A Program to display a Name ---')
print()

def printName(firstName):
    return (f'Hello {firstName}')

first_name= input('Enter the first Name: ')

print()

print(f'Your full name is {printName(first_name)}')

print()