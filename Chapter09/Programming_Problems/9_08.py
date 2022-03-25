# Write a menu driven program to read, display
# add, and subtract two complex numbers

class complex:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
    def add_complex(self, x1, x2):
        return x1 + x2
x1= complex(2,3)
x2 = complex(1,2)
comp = complex()
comp.add_complex()

sum = x1 + x2
print(sum)

    
    
