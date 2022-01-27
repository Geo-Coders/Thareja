# Write a function that accepts three integers,
# and returns True if any of the integers is 0, otherwise it returns False
print('------ A program that accepts three integers ------')
print()
def integers(a,b,c):
    if a==0 or b==0 or c== 0:
        return True
    else:
        return False

a = int(input('Enter the first number : '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number : '))
num = integers(a,b,c)
print(num)