#----- program 4.2 -----
# Write a program to determine the character entered by the user
char =  input('press any key :')
if char.isalpha():
    print('The user has entered a character')
if char.isdigit():
    print('The user has entered a digit')
if char.isspace():
    print('The user entered a white space character')
        
