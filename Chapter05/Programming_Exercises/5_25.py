# Write a program to reverse a string without using recursion

print('--- A program to reverse a string ---')
print()

def reverse_string(input_):
    ''' A Function that takes in a string then returns the reversed string '''
    string= ' '
    for char in input_:
        string= char + string
    return string

def main():
    ''' A function that contain the main body of the program '''
    input_= input('Enter a String to reverse: ')

    print()

    print(f'The original string is: {input_}')
    print(f'The reverse string is {reverse_string(input_)}')

    print()


if __name__ == '__main__':
    main()
