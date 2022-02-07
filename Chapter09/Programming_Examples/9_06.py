# Write a class Rectangle that has attributes Length and Breadth 
# and a method area which returns the area of the rectangle

class Rectangle:
    def get_data(self):
        Rectangle.length = int(input('Enter the length : '))
        Rectangle.breadth = int(input('Enter the breadth : '))
    def show_data(self):
        print(f'Length = {Rectangle.length}, \t Breadth = {Rectangle.breadth}')
    def area(self):
        print(f'Area = {Rectangle.length *Rectangle.breadth}')
rect = Rectangle()
rect.get_data()
rect.show_data()
rect.area()