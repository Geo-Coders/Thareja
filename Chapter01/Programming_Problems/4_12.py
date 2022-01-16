# Write a program that prints a number, it's square, and cube repeatedly in the range (1,n)

n = int(input('Enter a number : '))

for i in range (1, n+1):
    sqr = i**2
    cube = i**3

    print(f'The square of {i} is {sqr}')
    print(f'The cube of {i} is {cube}')
    print()
    
