# Write a program to reverse a string using recursion
print('------ A program to reverse string using recursion ------')
print()
def reverse(string):
    if len(string) ==0:
        return string
    else:
        return reverse(string[1:] + string[0])
input_= str(input('Enter the string to be reversed : '))
print(reverse(input_))
    