# Write a program to take input from the user and then check whether it is a number or a character. 
# if it is a character, determine whether it is in uppercase or lowercase.

ch= input('Enter a character: ')
if ch.isupper(): 
    print('Uppercase character was entered')
elif ch.islower():
    print('Lowercase character was entered')
elif ch.isnumeric:
    print('A number was enterd')
elif ch.isspace():
    print('Space is Entered')

print(f'{ch} is yet to be updated')