# Write a program that has a class Numbers with values stored in a list. Write a class method to find the largest value.

""" Program to use a constructor to create an array and find the largest element from that array"""
class Numbers:
    def __init__(self):
        self.values= []

    def find_max(self):
        max= ' '
        for i in self.values:
            if i > max:
                max= i
        print('Maximum element : {%r}' %max)

    def insert_element(self):
        value= input('Enter value : ')
        self.values.append(value)

x= Numbers()
ch = 'y'
while ch == 'y':
    x.insert_element()
    ch= input('Do you wish to enter more elements? ')

x.find_max()