#------- program 4.26 ------
# Write a program to calculate GCD of two numbers

num1 = int(input('Enter the two numbers : '))
num2 = int(input('Enter the two numbers : '))
if num1 > num2:
    dividend = num1
    divisor = num2
else:
    dividend = num2
    divisor = num1
while divisor != 0:
    remainder = dividend % divisor
    dividend = divisor
    divisor = remainder
print(f'GCD of {num1} and {num2} is {dividend}')