# A program that overloads the -= and /= operators in COMPLEX class. 
# The program must throw an exception if divide by zero exception occurs or if the real part of the two objects are zero 

print('--- A Program to overload -= and /= operators in complex class---')
print()
class Complex:
    def __init__(self, num):
        self.num= num
