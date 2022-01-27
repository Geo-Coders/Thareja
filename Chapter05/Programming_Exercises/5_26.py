# Write a program to calculate exp(x,y) using recursion
print('------ A program to calculate exp(x,y) using recursion ------')
print()
def exp_rec(x,y):
    if y == 0:
        return 1
    else:
        return (x * exp_rec(x, y-1))
n = int(input('Enter the first number : '))
m = int(input('Enter the second number : '))
print(f'Result = {exp_rec(n,m)}')