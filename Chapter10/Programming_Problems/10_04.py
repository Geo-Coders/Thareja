# Define a class Employee with data members as empno, name, and designation
# Derive a class Qualification from Employee that has data member UG, PG and experience. 
# Create another class Salary which is derived from both these classes to display details of the employee
# And compute their increments based on their experience and educational qualification




class Employee:
    def __init__(self):
        self.empno = int(input('Enter Employee no : '))
        self.name = input('Enter the employee name : ')
        self.designation = input('Enter the designation of the employee : ')
    def display(self):
        print(f'Emp  No : {self.empno}, Name : {self.name}, Designation : {self.designation}')
        
class Qualification(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.UG = input('Enter if UG is your highest level of education (y/n) : ')
        self.PG = input('Enter if PG is your highest level of education (y/n) : ')
        self.experience = int(input('Enter the years of experience : '))
    def display(self):
        Employee.display(self)
        print(f'UG : {self.UG}, PG : {self.PG}, Experience : {self.experience}')

         
class Salary( Qualification, Employee):
 
    def __init__(self):
        Qualification.__init__(self)
        self.salary = int(input('Enter the amount of salary : '))
        print(f'Salary : {self.salary}')
    def display(self):
        Qualification.display(self)
        
        if self.UG == 'y' and self.experience >= 5:
            increment = self.salary * 0.1
        elif self.UG== 'y' and self.experience <5:
            increment = self.salary * 0.05
        elif self.PG == 'y' and self.experience >= 5:
            increment = self.salary * 0.3
        elif self.PG == 'y' and self.experience < 5:
            increment = self.salary * 0.2
            Total_salary = increment + self.salary
            print(f'Total Salary : {Total_salary}')
        else:
            increment = 0
            Total_salary = increment + self.salary
            print(f'Total Salary : {Total_salary}')
        
       

s = Salary()

s.display()