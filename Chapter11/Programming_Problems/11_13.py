# Write a menu driven program to overload +=, -=, ==, >= and <=
# operators on the Fraction class.

print('--- Operator Overloading on Fraction Class ---')
print()

def GCD(num,deno):
    if deno == 0:
        return num
    else:
        return GCD(deno, num%deno)
class Fraction:
    def __init__(self, num, deno):
        self.num= num
        self.deno= deno

    def __isub__(self, other):
        Temp= Fraction(0,0)
        Temp.num= (self.num*other.deno) - (other.num*self.deno)
        Temp.deno= self.deno*other.deno   
        return Temp

    def __iadd__(self, other):
        Temp= Fraction(0,0)
        Temp.num= (self.num*other.deno) + (other.num*self.deno)
        Temp.deno= self.deno*other.deno   
        return Temp
    
    def __eq__(self, other):
            if isinstance(other, Fraction):
                self_= self.num + self.deno
                other_= other.num + other.deno
                return self_== other_
            return False

    def __ge__(self, other):
        if isinstance(other, Fraction):
            self_= self.num + self.deno
            other_= other.num + other.deno
            return self_>= other_
        return False

    def __le__(self,other):
        if isinstance(other, Fraction):
            self_= self.num + self.deno
            other_= other.num + other.deno
            return self_<= other_
        return False
    
    def __str__(self):
        self._simplfy()
        return (f'{self.num} / {self.deno}')

    def _simplfy(self):
        common_divisor= GCD(self.num, self.deno)
        self.num //= common_divisor
        self.deno //= common_divisor
    
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

        num0= int(input('Enter the first numerator : '))
        deno0= int(input('Enter the first denominator : '))
        var1= Fraction(num0,deno0)

        num1= int(input('Enter the second numerator : '))
        deno1= int(input('Enter the second denominator : '))
        var2= Fraction(num1,deno1)
        
        var1 += var2
        print(f'The answer is : {var1}')

    elif choice_ == '2':
        print()
        print('--- Addition Option has been selected ---')
        print()
        num0= int(input('Enter the first numerator : '))
        deno0= int(input('Enter the first denominator : '))
        var1= Fraction(num0,deno0)
        num1= int(input('Enter the second numerator : '))
        deno1= int(input('Enter the second denominator : '))
        var2= Fraction(num1,deno1)
        var1 -= var2
        print(f'The answer is : {var1}')

    elif choice_ == '3':
        print()
        print('--- Equating Option has been selected ---')
        print()
        num0= int(input('Enter the first numerator : '))
        deno0= int(input('Enter the first denominator : '))
        var1= Fraction(num0,deno0)
        num1= int(input('Enter the second numerator : '))
        deno1= int(input('Enter the second denominator : '))
        var2= Fraction(num1,deno1)
        print(f'Is {var1} equal to {var2} : {var1 == var2}')
    
    elif choice_ == '4':
        print()
        print('--- Less than or Equal to Option has been selected ---')
        print()
        num0= int(input('Enter the first numerator : '))
        deno0= int(input('Enter the first denominator : '))
        var1= Fraction(num0,deno0)
        num1= int(input('Enter the second numerator : '))
        deno1= int(input('Enter the second denominator : '))
        var2= Fraction(num1,deno1)
        print(f'Is {var1} less than or equal to {var2} : {var1 <= var2}')
    
    elif choice_ == '5':
        print()
        print('--- Greater than or Equal to Option has been selected ---')
        print()
        num0= int(input('Enter the first numerator : '))
        deno0= int(input('Enter the first denominator : '))
        var1= Fraction(num0,deno0)
        num1= int(input('Enter the second numerator : '))
        deno1= int(input('Enter the second denominator : '))
        var2= Fraction(num1,deno1)
        print(f'Is {var1} greater than or equal to {var2} : {var1 >= var2}')
    else:
        print('Quiting the Program')
        break

    print()