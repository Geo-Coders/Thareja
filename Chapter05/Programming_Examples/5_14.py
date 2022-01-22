# Write a program to calculate GCD using recursive functions

def GCD(x, y):
    rem = x % y
    if rem == 0:
        return y
    else:
        return GCD(y, rem)
    
n = int(input('Enter the first number : '))
m = int(input('Enter the second number : '))
print(f'The GCD is {GCD(m,n)}')