# Write a program that prompts the user to enter a character (O,A,B,C,F)
# Using if-elif-else construct display Outstanding, Very good, Good, Average and Fail respectively
print('----- A program prompting the user to enter character O, A, B, C, F -----')
print()

char = input('Enter any character (O, A, B, C, F) : ') 
if char == 'O':
    print('Outstanding')
    
elif char == 'A':
    print('Very good')
    
elif char =='B':
    print('Good')
    
elif char == 'C':
    print('Average')
    
elif char == 'F':
    print('Fail')
else:
    print('Invalid character')