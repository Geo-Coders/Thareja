# Write a program that has class Circle
# Use a class variable to define the value of constant PI.
# Use this class to calculate area and circumference of a circle with specified radius

class Circle:
    PI = 3.14159
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return Circle.PI * self.radius * self.radius
    def circumference(self):
        return 2* Circle.PI * self.radius
C = Circle(7.5)
print(f'AREA = {C.area()}')
print(f'CIRCUMFERENCE = {C.circumference()}')