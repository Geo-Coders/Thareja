# Write a program that uses lambda function to multiply two numbers

print('----- This program uses lambda to multiply two numbers-----')
print()

x = int(input('Enter the first number :'))
y = int(input('Enter the second number :'))
product = lambda x,y : x * y
print(f'Product {product(x,y)}')
