# Write a program to find mean of two numbers belonging to two different objects of the same class

class integer:
    def __init__(self):
        self.x = int(input('Enter the first integer : '))
        
        self.y = int(input('Enter the second integer : '))
    def mean(self):
     
        self.mean = (self.x +self.y)/2
        print(self.mean)
        
m = integer()
m.mean()

        