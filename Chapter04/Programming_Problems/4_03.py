# Write a program that determines whether an alphabet, digit or 
# a whitespace was entered
print('--- A program to evaluate a character entered by the user ---')
print()
print('Enter -1 to quit the Program at any time\n')

input_= input('Enter any character value to evaluate as alphabet, digit or a whitespace: ')
while input_ != '-1':
    if input_.isalpha():
        print(f'{input_} is an alphabet')

    elif input_.isdigit():
        print(f'{input_} is an digit')

    elif input_.isspace():
        print(f'{input_} is an whitespace')

    else:
        print('The input character is yet to be determined')

    input_= input('Enter another character: ')