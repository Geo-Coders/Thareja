# Write a program to calculate exp(x,y) without using recursion

print('--- A Program to calculate Exponential ---')
print()



def exp(x,n):
    ''' A function to calculate value using sum of first n terms of Taylor Series '''
    sum = 1.0

    for i in range(n, 0, -1):
        sum = 1 + x * sum/i

    return sum

x= int(input('Enter the base number: '))
n= int(input('Enter the nth value: '))

print()
print(f'e^x = {round(exp(x,n),2)}')
print()
