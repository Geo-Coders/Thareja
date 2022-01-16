# Write a program that prints anumber, it's square, and cube repeatedly in the range (1,n)

n = int(input('Enter a number : '))

for i in range (1, n+1):
    sqr = i**2
    cube = i**3

print(f'The square of {n} is {sqr}')
print(f'The cube of {n} is {cube}')

# Write a program that displays oxford university press as
# oxford university press
# OXFORD UNIVERSITY PRESS
# oXFORD UNIVERSITY PRESS


name = 'Oxford University Press'
print(name.lower())
print(name.upper())
print(name.swapcase()) 

# Write a program to read a floating point number and an integer
# If the value of the floating point number is greater than 4.14 then add 10 to the integer

num1 = float(input('Enter a floating number : '))
num2 = int(input('Enter an integer : '))
if num1 > 4.14:
    num2 = num2 + 10
    print(num2)
else:
    print(num2)
    
    num = 1
for i in range(5):
    for j in range(i+1):
        print(num, end=" ")
        num +=1
    print() 
    
# Write a program to display the sin(x) value 
# where x ranges from 0 to 360 in steps of 15

from cmath import sin
import math


for i in range(0, 361, 15):
    print(sin (i), end = ' ')
