# Write a program that prompts the user to enter five words. 
# If the length of any word is less than 6 characters, then it asks the user to enter it again
# However, if the word is of 6 or more character, then it displays it on the screen
print('------- A program to input 6 character word ------' )
print()

for i in range (1,6):
    input_ = input('Enter a word: ')
    while len(input_) < 6:
        
        print('Enter words with more than 6 characters')
        input_ = input('Enter another word: ')
        
    else:
        print(input_)
            
            
       
    