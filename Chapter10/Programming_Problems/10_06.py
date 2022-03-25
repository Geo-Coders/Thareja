# Write a program that has a class Person. 
# Derive Baseball_player from person 
# and display all the details of a famous baseball player

class Person:
    def __init__(self, name, age, medals):
        self.name = name
        self.age = age
        self.medals = medals
    def display(self):
        print(f'Name : {self.name} \n Age : {self.age} \n Medals : {self.medals}')
        
class Baseball_player(Person):
    def __init__(self, name, age, medals, years):
        Person.__init__(self, name, age, medals)
        self.years = years
    def display(self):
        Person.display(self)
        print(f'Years of experience: {self.years}')
                  
player = Baseball_player('james', 29, 10, 5)
player.display()
        
        
        