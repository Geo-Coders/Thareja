# Make a class Triangle. Enter its three sides and calculate its area
class Triangle:
    def get_data (self):
        Triangle.base = int(input('Enter the base : '))
        Triangle.height = int(input('Enter the height : '))
    def area(self):
        print('Area = : ',0.5 * Triangle.base*Triangle.height)
        
tri = Triangle()
tri.get_data()
tri.area()

        