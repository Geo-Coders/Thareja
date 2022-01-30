# Write a program that overloads the + operator to add 
# two objects of class Time


print('--- A Program to Overload the + Operator ---')
print()

class Time:
    def __init__(self):
        self.h0= int(input('Enter the Hour : '))
        self.m0= int(input('Enter the minutes : '))

    def __add__(self,other):
        h0= self.h0 + other.h0
        m0= self.m0 + other.m0

        total_time = (h0 + (m0/60))

        return round(total_time,2)


t0= Time()

t1= Time()


t2= t0 + t1
print(t2)