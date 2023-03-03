# A program to write a class Student. Use exception handling to read the data of a student

print('--- A Program to read data of a student using exception handling---')
print()

class Student:
    def __init__(self, name, eoll_no):
        self.name = name
        self.course = roll_no
    def display(self):
        print(self.name, ":", self.roll_no)

try:
    name = input('Enter your name : ')
    if len(name)==0:
        raise Exception
    roll_no = int(input('Enter your roll_no : '))
    if roll_no == 0:
        raise Exception
except Exception:

    print('The data entered does not exist in our database')
else:
    print("Welcome to your student portal")
    
            
    
            
        