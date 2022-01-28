# Write a program that has a class fraction with attributes numerator and
# denominator. Enter the values of the attributes and print the fraction 
# simplified form.

class fraction:
    def get_data(self):
        self.__num= int(input('Enter the numerator : '))
        self.__deno= int(input('Enter the denominator : '))
        if self.__deno == 0:
            print('Fraction not possible')
            exit()

    def display_data(self):
        self.__simplify()
        print(f'{self.__num}/{self.__deno}')

    def __simplify(self):
        print('The simplified fraction is : ')
        common_divisor= self.__GCD(self.__num, self.__deno)
        self.__num= self.__num/common_divisor
        self.__deno= self.__deno/common_divisor

    def __GCD(self, a,b):
        if b==0:
            return a
        else:
            return self.__GCD(b, a%b)

f= fraction()
f.get_data()
f.display_data()