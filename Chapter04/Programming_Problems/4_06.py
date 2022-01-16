# Write a program that prompts the user to enter a number.
# If the number is equal to 99, print 'Congratulations'
# If the number is less tha 99, print- enter again and aim higher
# Else print enter again a lower number. 
# The program should run until the user guesses the correct the number 99 that is

num = int(input('Guess a number : '))
while num != 99:
    
    if num < 99:
        print('Aim a higher number')
    else:
        print('Aim a lower number')
        
    num = int(input('Guess again another number : '))  

print()  
print('***************************************************')   
print('CONGRATULATIONS !!! You guessed the correct number.')
print()
print('***************************************************')