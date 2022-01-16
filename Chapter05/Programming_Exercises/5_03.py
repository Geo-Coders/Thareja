# Write a function that returns the absolute value of a number

print('--- A Program to Print the absolute value of a number ---')
print()

def abs_1(x):
    ''' A function that takes an integer then returns an absolute value '''
    return abs(x)


def main():
    ''' This function contain the main body of the program '''
    a = int(input("Enter any number to evaluate: "))
    print()
    print(f"The absolute value of the {a} is : {abs_1(a)}.")
    print()

if __name__ == '__main__':
    main()