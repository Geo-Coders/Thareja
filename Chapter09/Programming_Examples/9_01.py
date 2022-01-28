# Write a program that uses class to store the name and marks of students.
# Use list to store the marks in three subjects.

class Students:
    def __init__(self, name):
        self.name= name
        self.marks= []

    def enterMarks(self):
        for i in range(3):
            m= int(input(f'Enter the marks of {self.name} in subject {i+1} : '))
            self.marks.append(m)

    def display(self):
        print(f'{self.name} got {self.marks}')

s1= Students('Anisha')
s1.enterMarks()

s2= Students('Jignesh')
s2.enterMarks()

print()

s1.display()
s2.display()