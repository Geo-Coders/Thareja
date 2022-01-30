# Write a python program to get a string from a given string 
# Where all occurrences  of it's first character have been changed to $ 
# Except the first character itself
print('----- program to change a string  -----')
print()

def replace_char(str):
    char = str[0]
    str = str.replace(char, '$')
    str = char + str[1:]
    return str
str = input('Enter a string: ')
new_str = replace_char(str)
print(new_str)
    


