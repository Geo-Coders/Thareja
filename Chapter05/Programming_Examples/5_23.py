# Write a program that uses the getpass module to prompt 
# the user for a password, without echoing what they type to 
# the console

import getpass

password= getpass.getpass(prompt='Enter the password: ')
print()
if password == 'oxford':
    print('Welcome to the world of python Programming.')
else:
    print('Incorrect password... Sorry, you cannot read out book')
