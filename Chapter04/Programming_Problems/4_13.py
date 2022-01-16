# Write a program that prompts the user to enter a string. 
# The Program calculates and displays the length of the string 
# until the user enters "QUIT".(Hint: use a while loop)

print('--- A Program to evaluate the lenth of a string ---')
print()
print('Enter the word "QUIT" to quit')

input_string= input('Enter the string to evaluate: ') 

while input_string.upper() != 'QUIT':
    string_length= len(input_string)
    print(f'"{input_string}" has the length of {string_length} characters')
    
    print()

    input_string= input('Enter another string: ')

print('\nThe Program Has Been Terminated! \nBYE!!!!')











