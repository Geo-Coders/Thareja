# Write a program that overloads the + operator on a class Student
# that has attributes name and marks.

class Student:
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks

    def display(self):
        print(f'{self.name},{self.marks}')

    def __add__(self, S):
        Temp= Student(S.name, [])
        for i in range(len(self.marks)):
            Temp.marks.append(self.marks[i] + S.marks[i])
        return Temp

s1= Student('Nikhil', [87,90,85])
s2= Student('Nikhil', [83,86,88])
s1.display()
s2.display()

s3= Student('',[])
s3 = s1 + s2
s3.display()
