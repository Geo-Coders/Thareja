# Add a method reflect_x to class Point, which returns a new point
# which is the reflection of the point about the x-axis
# for example, point(7,8) reflect_x is point(7,-8)

from re import X


class Point:
    def reflect_x(self, x, y):
        self.x = x
        self.y = y
        print(self.x, self.y)
    def reflection(self):
        self.x = -x
        
    
