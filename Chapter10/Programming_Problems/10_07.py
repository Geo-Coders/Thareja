# Write a Program that extends the class Shape to calculate the area of a circle and cone.
# (Hint: To calculate area of a circle only one variable is required so when createing object,
#  pass the other variable with value 1)


print('--- A Program to Extend the class Shape ---')
print()

class Shape:
    def get_data(self):
        raise NotImplementedError()

    def area(self):
        raise NotImplementedError()

class Circle(Shape):
    def get_data(self):
        self.radius= float(input('Enter the radius of the Circle : '))

    def area(self):
        import math
        return (math.pi * (self.radius ** 2))

class Cone(Shape):
    def get_data(self):
        self.radius =  float(input('Enter the radius of the Cone : '))
        self.height= float(input('Enter the Height of the Cone : '))

    def area(self):
        import math
        return ((math.pi * self.radius * self.height) + (math.pi * (self.radius**2)))



R= Circle()
R.get_data()
print(f'Area of Circle : {round(R.area(),2)} squared units')

T= Cone()
T.get_data()
print(f'Area of Cone : {round(T.area(),2)}squared units')

