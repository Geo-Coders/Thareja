# Write a program that has a class student that stores roll number, name and marks
# (in three subjects) of the students. Display the information
# (roll number, name and total marks) stored about the student.

class student:
    __marks= []
    def set_data(self, r,n,m1,m2,m3):
        student.__rollno = r
        student.__name= n
        student.__marks.append(m1)
        student.__marks.append(m2)
        student.__marks.append(m3)

    def display_data(self):
        print('Student Details')
        print(f'Roll Number : {student.__rollno}')
        print(f'Name : {student.__name}')
        print(f'Marks : {self.total()}')

    def total(self):
        m= student.__marks
        return m[0] + m[1] + m[2]

r= int(input('Enter the roll number : '))
n= input('Enter the name : ')
m1= int(input('Enter the marks in first subject : '))
m2= int(input('Enter the marks in second subject : '))
m3= int(input('Enter the marks in third subject : '))

s1= student()
s1.set_data(r,n,m1,m2,m3)
s1.display_data()