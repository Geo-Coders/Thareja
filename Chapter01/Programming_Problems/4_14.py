# Write a program that prompts the user to enter five words. 
# If the length of any word is less than 6 characters, then it asks the user to enter it again
# However, if the word is of 6 or more character, then it displays it on the screen

i = 1

while i <= 5:
    input_ = input('Enter a word: ')
    if len(input_) < 6:
        print('Enter words with more than 6 characters')
    else:
        print(input_)
        i = i+1
    