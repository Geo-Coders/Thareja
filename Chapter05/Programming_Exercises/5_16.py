# Write a menu driven program using functions to perform calculator operations 
# such as adding, subtracting, multiplying, and dividing two integers

print('----- A program to perform calculator operations ')
print()

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x -y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print('Select operation')
print('n\t1.Addition')
print('n\t2.Subtraction')
print('n\t3.Multiplication')
print('n\t4.Division')
print('n\t6.Exit')

choice = int(input('select a choice : '))


if choice == 1:
    number1 = int(input('Enter the first number : '))
    number2 = int(input('Enter the second number : '))
    s = add(number1, number2)
    print(f'The sum is {s}')
    
elif choice == 2:
    number1 = int(input('Enter the first number : '))
    number2 = int(input('Enter the second number : '))
    d = subtract(number1, number2)
    print(f'The difference is {d}')
    
elif choice == 3:
    number1 = int(input('Enter the first number : '))
    number2 = int(input('Enter the second number : '))
    m = multiply(number1, number2)
    print(f'The product is {m}')
    
elif choice == 4:
    number1 = int(input('Enter the first number : '))
    number2 = int(input('Enter the second number : '))
    d= divide(number1, number2)
    print(f'The answer is {d} ')
else:
    print('Exiting the calculator')
    
    

    

    