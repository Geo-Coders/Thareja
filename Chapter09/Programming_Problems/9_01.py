# Write a program that has a class Point with attributes as the X and Y
# co-ordinates. Make two objects of this class and find the midpoint of 
# both the points

print('--- A Program to find the mid of two points ---')
print()


class Point:
    def __init__(self):
        self.x1 = int(input('Enter the value of x1 : '))
        self.y1 = int(input('Enter the value of y1 : '))
        self.x2 = int(input('Enter the value of x2 : '))
        self.y2 = int(input('Enter the value of y2 : '))

    def is_midpoint(self):
        self.a = (self.x1 + self.x2)/2
        self.b = (self.y1 + self.y2)/2
        return f'({self.a},{self.b})'

p = Point()
print(f'The midpoint of the line is {p.is_midpoint()}')
