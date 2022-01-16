# Write a program to swap two variables that are defined as global variables.

from cgi import print_directory


print('--- A Program to swap two variables ---')
print()


def swap_numbers(a,b):
    ''' A function takes two integers then returns the swapped values'''
    temp= a
    a= b
    b= temp
    return (f'({a},{b})')


def main():
    ''' This function contain the main body of the program '''
    first_number= eval(input('Enter the first number: '))
    second_number= eval(input('Enter the second number: '))
    print()
    print(f'Before Swapping two Numbers ({first_number},{second_number})')
    print(f'After Swapping two numbers {swap_numbers(first_number,second_number)}')
    print()


if __name__ == '__main__':
    main()
