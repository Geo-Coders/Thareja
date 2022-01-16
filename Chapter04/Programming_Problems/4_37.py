# Write a program that accepts any number and prints the number of digits in that number

print('--- A Program to print the number of digits in an enterd number by the user ---')
print()
print('Enter -1 to quit the program')

number= int(input('Enter any number to evaluate: '))
while number != -1:
    print(f'{number} has {len(str(number))} digits')
    print()
    number= int(input('Enter another number: '))