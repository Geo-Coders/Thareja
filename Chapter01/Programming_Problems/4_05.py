# Write a program that counts the number of lowercase characters,
# uppercase characters and digits entered by the user

print('--- This is a character counter Program ---')
print()
print('Enter -1 to quit the Program at any time\n')

digit_counter= lowercase_counter= uppercase_counter= 0 

input_= input('Enter the character to : ')
while input_ != '-1':
    if input_.isdigit():
        digit_counter += 1

    elif input_.isupper():
        uppercase_counter += 1

    elif input_.islower():
        lowercase_counter += 1

    else:
        print('Enter a valid character: ')

    input_= input('Enter the character to evaluate: ')

print(f'{digit_counter} digit characters entered')
print(f'{lowercase_counter} lowercase characters entered')
print(f'{uppercase_counter} uppercase characters entered')