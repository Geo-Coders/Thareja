# Write a menu driven program to overload +=, -=, ==, >= and 
# <= operators on the Distance class

print('--- Operator Overloading on Distance Class ---')
print()

class Distance:
    def __init__(self):
        self.km= 0
        self.m= 0

    def set(self, km, m):
        self.km= km
        self.m= m

    def __isub__(self, other):
        self.m -= other.m
        if self.m < 0:
            self.m += 1000
            self.km -= 1

        self.km -= other.km

        return self