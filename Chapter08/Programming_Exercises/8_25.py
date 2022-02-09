# Write a program that prompts the user to enter an
# alphabet. Print all the words in the list that starts with that 
# alphabet..

print('--- A Program to display words that starts with with a given alphabet ---')
print()

St= input('Enter the Sentence to evaluate : ')
char_= input('Enter the character of words to return : ')
for i in St.split():
    if i.startswith(char_):
        print(i)

print()