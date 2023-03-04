# Write a menu driven program to read, display
# add, and subtract two complex numbers

class complex():
    def initComplex(self):
        self.real_part = int(input("Enter the real part : "))
        self.img_part = int(input("Enter the imaginary part : "))
    
        
    def display(self):
        print(self.real_part, "+", self.img_part, "i", sep ="")
    def sum(self, c1,c2):
        self.real_part = c1.real_part + c2.real_part
        self.img_part = c1.img_part + c2.img_part
    def subtract(self, c1, c2):
        self.real_part = c1.real_part - c2.real_part
        self.img_part = c1.img_part - c2.img_part
        
c1 = complex()
c2 = complex()
c3 = complex()

c1.initComplex()
c1.display

c2.initComplex()
c2.display

c3.display()
c3.sum(c1.c2)    
        




    
    
