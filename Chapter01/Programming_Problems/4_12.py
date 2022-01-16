# Write a program that prints anumber, it's square, and cube repeatedly in the range (1,n)

n = int(input('Enter a number : '))

for i in range (1, n+1):
    sqr = i**2
    cube = i**3
    
print(f'The square of {n} is {sqr}')
print(f'The cube of {n} is {cube}')
    