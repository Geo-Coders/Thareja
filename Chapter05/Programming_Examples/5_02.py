# Write a program to swap two numbers

def swap(a,b):
    a,b = b,a
    print('After swap : ')
    print(f'First number = {a}')
    print(f'Second number = {b}')
      
a = input('\n Enter the first number : ')
b = input('\n Enter the second number : ')
print('Before swap : ')
print(f'first number = {a}')
print(f'Second number = {b}')
swap(a,b)
