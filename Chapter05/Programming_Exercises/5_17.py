# Write a program using a function that calculates the hypotenuse of a right-angled triangle

print('--- A Program that calculates hypotenues of a right-angle triangle ---')
print()


def hypotenus(a,b):
    ''' A function that takes two integers then returns the hypotenus '''
    import math
    x = (a**2) + (b**2)
    return math.sqrt(x)


def main():
    ''' A function that contain the main body of the program '''
    a = int(input("Enter the height of the triangle : "))
    b = int(input("Enter the length of the triangle : "))
    print()
    print("The Hypotenus of the Triangle is :", hypotenus(a,b))
    print()


if __name__ == '__main__':
    main()

