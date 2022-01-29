# write a program prompts the user to enter two numbers and displays their sum
# Raise an exception and handle it if a non-number value is given as input

print('--- A Program to display the sum of two given numbers ---')
print()

try: 
    num0 = int(input('Enter the first Number : '))
    num1 = int(input('Enter the second Number : '))

    if num0:
        if num1:
            sum = num0 + num1
            print(f'The Sum of {num0} and {num1} is : {sum}')

        else:
            raise ValueError

    else:
        raise ValueError

except ValueError:
    print('A non number value has been detected')

else:
    print('Thank you for your Time!')


print()