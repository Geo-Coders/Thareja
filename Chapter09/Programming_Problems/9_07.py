# Write a menu driven program to read, display, simplify, add
# and subtract two fractions.

print('--- A Program to work on fractions ---')
print()

class Faction:
    def __get_data(self):
        self.__num = int(input('Enter the Numerator : '))
        self.__deno0 = int(input('Enter the Denominator : '))
        if (self.__deno0 == 0):
            print('Fraction not possible')
            exit()

    def __GCD(self, a,b):
        if b == 0:
            return a
        else:
            return self.__GCD(b,a%b)

    def __LCM(self,a,b):
        lcm = (a*b)/self.__GCD(a,b)
        return lcm

    def simplify(self):
        self.__get_data()
        common_divisor = self.__GCD(self.__num,self.__deno0)
        self.__num = self.__num/common_divisor
        self.__deno0 = self.__deno0/common_divisor
        print(f'The simplified fraction is : {self.__num}/{self.__deno0}')

    def add(self):
        self.__deno1 = int(input('Enter the first denominator : '))
        self.__deno2 = int(input('Enter the second denominator : '))
        self.__add1 = (self.__deno1 + self.__deno2)/self.__LCM(self.__deno1,self.__deno2)        
        print(f'The Addition of (1/{self.__deno1} + 1/{self.__deno2}) is : {self.__add1}')

    def subtraction(self):
        self.__deno1 = int(input('Enter the first denominator : '))
        self.__deno2 = int(input('Enter the second denominator : '))
        if self.__deno1 > self.__deno2:
            self.__add1 = (self.__deno1 - self.__deno2)/self.__LCM(self.__deno1,self.__deno2)        
            print(f'The Addition of (1/{self.__deno1} - 1/{self.__deno2}) is : {self.__add1}')

        else:
            self.__add1 = (self.__deno2 - self.__deno1)/self.__LCM(self.__deno1,self.__deno2)        
            print(f'The Addition of (1/{self.__deno2} - 1/{self.__deno1}) is : {self.__add1}')

while True:
    print("""
    1. Addition
    2. Subtraction
    3. Simplification
    """)
    choice = int(input('Enter the choice by selecting the number, from the Menu given Above : '))
    if choice == 1:
        f = Faction()
        f.add()
        
    elif choice == 2:
        f = Faction()
        f.subtraction()
        
    elif choice == 3:
        f = Faction()
        f.simplify()
    else:
        print('Invalid Choice!')
        
    ch = input('Would you wish to continue(y/n)? : ')
    if ch == 'n':
        break

print('Thank you for your time!')
