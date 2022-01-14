# Write a program to print the multiplication table of n, where n is entered by the user

n = int(input('Enter any number : '))
print(f'Multiplication table of {n}')
print('**************************************')
for i in range (1, 11):
    print(f'{n} X {i} = {n*i}')
