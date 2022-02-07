# Write a proram with class employees that keeps a track of the number of employees in an organization 
# and also stores their name, designation and salary details

class Employee:
    empcount = 0
    def __init__(self, name, desig, salary):
        self.name = name
        self.desig = desig
        self.salary = salary
        Employee.empcount += 1
        
    def displayCount(self):
        print(f'There are {Employee.empcount} employees')
    def displayDetails(self):
        print(f'Name : {self.name}, Designation : {self.desig}, Salary : {self.salary} ')
        
e1 = Employee('Farhan', 'Manager', 100000)
e2 = Employee('Mike', 'Team Leader', 90000)
e3 = Employee('Niyam', 'Programmer', 80000)
e4 = Employee('Ojas', 'Office Assistant', 60000)
e4.displayCount()
print('Details of second employee - \n')
e2.displayDetails()