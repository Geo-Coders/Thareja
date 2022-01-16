# Write a program that passes lambda function as an argument 
# to another function to compute the cube of a number

print('--- A Program to compute a cube of a number ---')
print()

def cube(a):
    ''' A function to return a cube of a number '''
    return (lambda x: x**3)(a)

def main():
    ''' This function contain the main body of the program '''
    b = int(input("Enter a number to compute: "))
    print()
    print(f"The Cube of {b} is : {cube(b)}")
    print()

if __name__ == '__main__':
    main()