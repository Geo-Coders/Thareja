# Write a program that overloads the /= operator in Fraction class.
# Throw an exception if a divide by zero exception occurs.


print('--- A Program to display Operator Overload in Fraction Class ---')
print()

class Fraction:
    def __init__(self, num):
        self.num= num

    def __itruediv__(self, other):
        try: 
            self.num /= other
            print('Computed!')
        
        except ZeroDivisionError:
            print('The Second number cannot never be 0')


test = Fraction(2)

test /= 10
 
print()