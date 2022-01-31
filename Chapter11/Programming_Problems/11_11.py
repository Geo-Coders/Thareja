# Write a menu driven program to overload +=, -=, ==, >= and <=
# operators on the Complex class.

print('--- Operator Overloading on Complex Class ---')
print()

class Complex:
    def __init__(self, real, image):
        self.real= real
        self.image= image

    def __isub__(self, other):
        self.real -= other.real
        self.image -= other.image    
        return Complex(self.real, self.image)

    def __iadd__(self, other):
        self.real += other.real
        self.image += other.image    
        return Complex(self.real, self.image)
    
    def __eq__(self, other):
            if isinstance(other, Complex):
                self_= self.real + self.image
                other_= other.real + other.image
                return self_== other_
            return False

    def __ge__(self, other):
        if isinstance(other, Complex):
            self_= self.real + self.image
            other_= other.real + other.image
            return self_>= other_
        return False

    def __le__(self,other):
        if isinstance(other, Complex):
            self_= self.real + self.image
            other_= other.real + other.image
            return self_<= other_
        return False
    
    def __str__(self):
        return (f'{self.real} + {self.image}i')
    

print('Enter Your choice from the given Menu to quit the Program Enter \'quit\'')
while True:
    print('1. <= Addition =>')
    print('2. <= Subtraction =>')
    print('3. <= Equating two inputs =>')
    print('4. <= Less Than =>')
    print('5. <= Greater Than =>')

    choice_= (input('Choose a number from the given options above : '))

    while True:
        if choice_.lower() not in ['1','2','3','4','5','quit']:
            choice_= (input('Invalid Input, Please Choose a valid Number : '))
            print()
        else:
            break
    
    if choice_ == '1':
        print()
        print('--- Addition Option has been selected ---')
        print()

        real0= int(input('Enter the first real number : '))
        image0= int(input('Enter the first imaginary number : '))
        var1= Complex(real0,image0)

        real1= int(input('Enter the second real number : '))
        image1= int(input('Enter the second imaginary number : '))
        var2= Complex(real1,image1)
        
        var1 += var2
        print(f'The answer is : {var1}')

    elif choice_ == '2':
        print()
        print('--- Addition Option has been selected ---')
        print()
        real0= int(input('Enter the first real number : '))
        image0= int(input('Enter the first imaginary number : '))
        var1= Complex(real0,image0)
        real1= int(input('Enter the second real number : '))
        image1= int(input('Enter the second imaginary number : '))
        var2= Complex(real1,image1)
        var1 -= var2
        print(f'The answer is : {var1}')

    elif choice_ == '3':
        print()
        print('--- Equating Option has been selected ---')
        print()
        real0= int(input('Enter the first real number : '))
        image0= int(input('Enter the first imaginary number : '))
        var1= Complex(real0,image0)
        real1= int(input('Enter the second real number : '))
        image1= int(input('Enter the second imaginary number : '))
        var2= Complex(real1,image1)
        print(f'Is {var1} less than or equal to {var2} : {var1 == var2}')
    
    elif choice_ == '4':
        print()
        print('--- Less than or Equal to Option has been selected ---')
        print()
        real0= int(input('Enter the first real number : '))
        image0= int(input('Enter the first imaginary number : '))
        var1= Complex(real0,image0)
        real1= int(input('Enter the second real number : '))
        image1= int(input('Enter the second imaginary number : '))
        var2= Complex(real1,image1)
        print(f'Is {var1} less than or equal to {var2} : {var1 <= var2}')
    
    elif choice_ == '5':
        print()
        print('--- Greater than or Equal to Option has been selected ---')
        print()
        real0= int(input('Enter the first real number : '))
        image0= int(input('Enter the first imaginary number : '))
        var1= Complex(real0,image0)
        real1= int(input('Enter the second real number : '))
        image1= int(input('Enter the second imaginary number : '))
        var2= Complex(real1,image1)
        print(f'Is {var1} less than or equal to {var2} : {var1 >= var2}')
    else:
        print('Quiting the Program')
        break

    print()