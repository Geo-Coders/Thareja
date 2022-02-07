# Write a program to change a given string to a new string where the first and last character have been changed
print('---- A program to change string by interchanging characters ----')
print()

def change_string(str):
    return str[-1]+ str[1:-1] + str[1]
str = input('Enter a string : ')
changed_string = change_string(str)
print(changed_string)