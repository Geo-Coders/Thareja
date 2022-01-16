# Write a program using a function that calculates the hypotenuse of a right-angled triangle

print('--- A Program that calculates hypotenuse of a right-angle triangle ---')
print()


def hypotenuse(a,b):
    ''' A function that takes two integers then returns the hypotenuse '''
    import math
    x = (a**2) + (b**2)
    return math.sqrt(x)


def main():
    ''' A function that contain the main body of the program '''
    a = int(input("Enter the height of the triangle : "))
    b = int(input("Enter the length of the triangle : "))
    print()
    print("The Hypotenuse of the Triangle is :", hypotenuse(a,b))
    print()


if __name__ == '__main__':
    main()

