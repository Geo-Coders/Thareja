# Write a program to read two points and calculate the distance between them
class Points:
     
    def __init__(self):
         
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
    
    def read(self):
        self.x1 = int(input('Enter the value of x1 : '))
        self.y1 = int(input('Enter the value of y1 : '))
        self.x2 = int(input('Enter the value of x2 : '))
        self.y2 = int(input('Enter the value of y2 : '))
        
    def distance(self):
         distance = ((((self.x2 - self.x1)**2 + (self.y2 - self.y1) **2)) **0.5)
         
         print(f' The distance between the two points is {distance}')
    
p = Points()
p.read()
p.distance()