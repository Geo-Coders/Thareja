# A program to print the square root of a number
# Raise an exception if the number is negative

print('--- A Program to print the square root of a number---')
print()
from  math import sqrt

try:
    num = int(input("Enter a number : "))
    if num == -num:
        raise ValueError

except ValueError:
    print('Value Error has been caught!')

else:
    print(f"The square root of {num} is : ", sqrt(num))
        
        

