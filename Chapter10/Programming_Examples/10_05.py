# Write a program that has a class Person. Inherit a class Faculty from Person
# which also has a class Publications.

class Person:
    def __init__(self, name, age, sex):
        self.name= name
        self.age= age
        self.sex= sex

    def display(self):
        print(f'NAME : {self.name}')
        print(f'AGE : {self.age}')
        print(f'SEX : {self.sex}')

class Publications:
    def __init__(self, no_RP, no_Books, no_Art):
        self.no_RP= no_RP
        self.no_Books= no_Books
        self.no_Art= no_Art

    def display(self):
        print(f'Number of Research Papers Published : {self.no_RP}')
        print(f'Number of Books Published : {self.no_Books}')
        print(f'Number of Articles Published : {self.no_Art}')

class Faculty(Person):
    def __init__(self, name, age, sex, design, dept, no_RP, no_Books, no_Art):
        super(Faculty,self).__init__(name, age, sex)
        self.design= design
        self.dept= dept
        self.Pub= Publications(no_RP, no_Books, no_Art)

    def display(self):
        Person.display(self)
        print(f'DESIGNATION : {self.design}')
        print(f'DEPARTMENT : {self.dept}')
        self.Pub.display()

F= Faculty('Pooja', 38, 'Female', 'TIC', 'Computer Science', 22, 1, 3)
F.display()

