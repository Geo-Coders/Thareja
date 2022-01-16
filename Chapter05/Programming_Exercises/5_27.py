# Write a program to calculate exp(x,y) without using recursion

print('--- A Program to calculate Exponential ---')
print()



def exp(x,y):
    p = f = 1.0

    if y == 0: 
        return 1
    r = exp(x, y-1)

    p *= x
    f *= y

    return (r + (p/f))

x= int(input('Enter the base number: '))
y= int(input('Enter the power value: '))

print()
print(f'{round(exp(x,y),2)}')
print()
