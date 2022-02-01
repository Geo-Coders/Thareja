# Define a class Student with data members as rollno and name
# Derive a class Fees from student that has a data member fees and functions
# to submit fees and generate receipt. Derive another class Result from Student 
# that displays the marks and grade obtained by the student.

print('--- A Program to Implement Student Class ---')
print()

class student:
    def detail(self):
        self.roll_no= input('Enter the roll no of the student: ')
        self.name= input('Enter the name of the student: ')

class fees(student):
    fees= 75000
    def submit_fees(self):
        student.detail(self)
        submission= int(input('Enter the fees needs to be submitted : '))
        self.submission= submission
        self.remaning= fees.fees-submission
        if submission == fees.fees:
            print('*****RECEIPT******')
            self.reciept()
        else:
            print('Amount is low!!! ')
            print('Please pay the remaining amount under extended time of 2 months!!!')
            self.reciept()
            
   
    def reciept(self):
        
        print(f'Roll no: {self.roll_no}')
        print(f'Name : {self.name}')
        print(f'Fees deposited : {self.submission}')
        print(f'Remaining amount: {self.remaning}')

f= fees()
f.submit_fees()

