# Define a class Employee. Display the personal and salary details of five employees using single inheritance

class Employee:
    def get(self):
        self.name = input('Enter employee name : ')
        self.salary = int(input('Enter employee salary : '))
        
    
    def display_data(self):
        print(f'Name : {self.name} \n Salary : {self.salary}')
    

class Employee1(Employee):
    def get_employee_info(self):
        Employee.__init__(self )
        self.name = input('Enter second employee name : ')
        self.salary = int(input('Enter second employee salary : '))
       
    def display_data(self):
        Employee.display_data(self)
        print(f'Name : {self.name} \n Salary : {self.salary}')
        
class Employee2(Employee):
    def get_employee_info(self, ):
        Employee.__init__(self)
        self.name = input('Enter third employee name : ')
        self.salary = int(input('Enter third employee salary : '))
       
        
    
    def display_data(self):
        Employee.display_data(self)
        print(f'Name : {self.name} \n Salary : {self.salary}')
        
class Employee3(Employee):
    def get_employee_info(self, ):
        Employee.__init__(self)
        self.name = input('Enter fourth employee name : ')
        self.salary = int(input('Enter fourth employee salary : '))
       
        
    
    def display_data(self):
        Employee.display_data(self)
        print(f'Name : {self.name} \n Salary : {self.salary}')     
        
class Employee4(Employee):
    def get_employee_info(self):
        Employee.__init__(self)
        self.name = input('Enter fifth employee name : ')
        self.salary = int(input('Enter fifth employee salary : '))
        
    
    def display_data(self):
        Employee.display_data(self)
        print(f'Name : {self.name} \n Salary : {self.salary}')   
               
    
e =Employee()
e.get()
e.display_data()
e1 = Employee1()
e1.get_employee_info()
e1.display_data()
e2 = Employee2()
e2.get_employee_info()
e2.display_data()
e3 = Employee3()
e3.get_employee_info()
e3.display_data()
e4 = Employee4()
e4.get_employee_info()
e4.display_data()

