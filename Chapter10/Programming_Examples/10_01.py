# Write a program that has a class Point. Define another class Location
# which has two objects(Location and Destination) of class Point.
# Also define a function in Location that prints the reflection of 
# Destination on the x axis

class Point:
    def __init__(self, x,y):
        self.x= x
        self.y= y

    def get(self):
        return (self.x, self.y)

class Location:
    def __init__(self, x1, y1, x2,y2):
        self.Source= Point(x1,y1)
        self.Destination= Point(x2,y2)

    def show(self):
        print(f'Source = {self.Source.get()}')
        print(f'Destination = {self.Destination.get()}')

    def reflection(self):
        self.Destination.x= -self.Destination.x
        print(f'Reflection Point on x Axis is : {self.Destination.x, self.Destination.y}')

L= Location(1,2,3,4)
L.show()
L.reflection()