# Write a program that determines whether a digit, uppercase, or a lowercase character was entered

char = input('Enter a character : ')
if  char >= '0' and char <= '9':
    print(' A digit was entered')
    
elif char >= 'a' and char <= 'z':
    print('A lowercase character was entered')

elif char >= 'A' and char <= 'Z':
    print('An uppercase character was entered')
    
else:
    print('The character is neither a digit, an uppercase nor a lowercase')
    
    
    
