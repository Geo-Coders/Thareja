# Write a program that has an abstract class Polygon. Derive two classes Rectangle and Triangle from Polygon and write methods to get the detials of their dimensions
# and hence calculate the area

class Polygon:
    def get_data(self):
        raise NotImplementedError()

    def area(self):
        raise NotImplementedError()

class Rectangle(Polygon):
    def get_data(self):
        self.length= float(input('Enter the Length of the Rectangle : '))
        self.breadth= float(input('Enter the Breadth of the Rectangle : '))

    def area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    def get_data(self):
        self.base= float(input('Enter the Base of the Triangle : '))
        self.height= float(input('Enter the Height of the Triangle : '))

    def area(self):
        return 0.5*self.base*self.height

R= Rectangle()
R.get_data()
print(f'Area of Rectangle : {R.area()}')

T= Triangle()
T.get_data()
print(f'Area of Triangle : {T.area()}')