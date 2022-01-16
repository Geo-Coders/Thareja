# Write a program that finds the greatest of three given numbers
# using functions. Pass the numbers as arguments

print('--- A Program that returns greatest of the given numbers --')
print()

def greatest(x,y,z):
    """ This function takes 3 digit arguments and then returns the greatest number of the three."""
    return max(max(x,y),z)

def main():
    ''' This function contain the main body of the program '''
    x= eval(input('Enter the first number: '))
    y= eval(input('Enter the second number: '))
    z= eval(input('Enter the third number: '))

    print()

    print(f'The greatest number is {greatest(x,y,z)}')

    print()


if __name__ == '__main__':
    main()





