# Write a program that has a class Person storing name and date of birth(DOB)
# of a person. The program should subtract the DOB from today's to find out 
# whether a person is eligible to vote or not.

import datetime

class Person():
    def __init__(self, name, dob):
        self.name= name
        self.dob= dob

    def check(self):
        today= datetime.date.today()
        age= today.year - self.dob.year

        if today < datetime.date(today.year, self.dob.month, self.dob.day):
            age -= 1
        if age >= 18:
            print(f'{self.name}, Congratulations... Your are eligible to vote.')
        else:
            print(f'{self.name}, Sorry... You should be at least 18 years of age to cast your vote.')


P1= Person('Sasha', datetime.date(1998, 12, 11))
P1.check()
print()
P2= Person('Jamal Makame', datetime.date(1996,10,11))
P2.check()
