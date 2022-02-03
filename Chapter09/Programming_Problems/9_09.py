# Write a menu driven program to read, display, add, and subtract two distances.

print('--- A Program to manipulate Distance input ---')
print()

class Distance:
    def __init__(self):
        self.dist1 = ''
        self.dist2 = ''

    def get_data(self):
        self.dist1 = int(input('Enter the first distance : '))
        self.dist2 = int(input('Enter the second distance : '))

    def __add(self, a,b):
            self.dist1 += self.dist2
            return self.dist1

    def _sub(self,a,b):
        if a > b:
            self.dist1 -= self.dist2
            return self.dist1
        else:
            self.dist2 -= self.dist1
            return self.dist2

    def display(self):
            print(f'The addition of the distance between {self.dist1} and {self.dist2} is : {self.__add(self.dist1,self.dist2)}')
            print(f'The Subtraction of the two distances is : {self._sub(self.dist1,self.dist2)}')
            print('\n')
my_list = []
while True:
    print("""
    1. Read Distances
    2. Display
    """)
    choice = int(input('Enter the choice number : '))
    if choice == 1:
        d = Distance()
        d.get_data()
        my_list.append(d)

    elif choice == 2:
        for day in my_list:
            day.display()
    
    ch = input('Would you wish to continue(y/n)? : ')
    if ch != 'y':
        break

print('Thank you for your time!')


