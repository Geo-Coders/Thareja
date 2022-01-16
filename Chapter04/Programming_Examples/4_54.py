# Write a program to calculate the square root of a number. Demonstrate the use of break and continue statement

import math
total_prime = 0
total_composite = 0

while 1:
    num = int(input('Enter no. '))
    if num == 999:
        break
    elif num < 0:
        print('Square root of negative numbers cannot be calculated')
        continue
    else:
        print(f'Square root of {num} = {math.sqrt(num)}')
