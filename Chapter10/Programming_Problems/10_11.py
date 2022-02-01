# Write a Program that has a class Distance with members- Kms and metres.
# Derive classes School and Office which store the distance from your house 
# to school and office along with other details.


print('--- A Program to Implement Distance class ---')
print()

class Distance:
    def __init__(self):
        self.kms= ' '
        self.m= ' '

class School(Distance):
    def __init__(self):
        super().__init__()

    def get_data(self):
        self.name= input('What is the name of your school : ')
        self.choice= input('How far is your school in term of distance, choose--kms/m : ').lower()
        while True:
            if self.choice not in ['kms', 'm']:
                self.choice= input('Invalid choice, Choose kms or m : ').lower()
            else:
                break
        print()
        
    
    def display(self):
        _dist= int(input('Enter the distance to Your School : '))
        print(f'Your School Name is {self.name}')
        print(f'Your School distance is {_dist} {self.choice}')
        print()

class Office(Distance):
    def __init__(self):
        super().__init__()

    def get_data(self):
        self.name= input('What is the name of your place of Work : ')
        self.choice= input('How far is your school in term of distance, choose--kms/m : ').lower()
        while True:
            if self.choice not in ['kms', 'm']:
                self.choice= input('Invalid choice, Choose kms or m : ').lower()
            else:
                break
        print()

    def display(self):
        _dist= int(input('Enter the distance to Your Office : '))
        print(f'Your School Name is {self.name}')
        print(f'Your School distance is {_dist} {self.choice}')
        print()

    

P1= School()
P1.get_data()
P1.display()

P0= Office()
P0.get_data()
P0.display()


