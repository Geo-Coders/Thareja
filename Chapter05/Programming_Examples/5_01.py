# Write a program using functions to check whether two numbers are
# equal or not.

def check_relation(a,b):
    if a == b:
        return 0

    elif a > b:
        return 1

    else:
        return -1

a= int(input('Enter the first number: '))
b= int(input('Enter the second number: '))

res= check_relation(a,b)
if res == 0:
    print(f'{a} is equal to {b}')

elif res == 1:
    print(f'{a} is greater than {b}')

else:
    print(f'{a} is less than {b}')
