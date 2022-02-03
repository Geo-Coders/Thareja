# Write a program that uses a class attribute to define some default titles 
# for faculty in a college. Display the name along with title and department 
# of the college.

print('--- A Program for faculty in a college ---')
print()

class Person:
    def __init__(self, name, department, 
    title = 'Senior Lecturer'):
        self.name = name
        self.department = department
        self.title = title

    def display(self):
        print(f"""
        Name : {self.name.title()}
        Title : {self.title.title()}
        Department : {self.department.title()}
        """)

p = Person('Jamal Makame', 'physics department', 'junior lecturer')
p.display()
q = Person('Salum Makame', 'Chemistry Department')
q.display()