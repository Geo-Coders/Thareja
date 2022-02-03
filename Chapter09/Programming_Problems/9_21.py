# Write a menu driven program to read, add, subtract, multiply, 
# divide and transpose two matrices

print('--- A Program to manipulate two Matrices ---')
print()

import numpy

class Matrix:
    def read(self):
        while True:
            var1= int(input('Enter the first number of the Matrix : '))
            var2= int(input('Enter the second number of the Matrix : '))
            var3= int(input('Enter the third number of the Matrix : '))
            var4= int(input('Enter the forth number of the Matrix : '))
            var5= int(input('Enter the fifth number of the Matrix : '))
            var6= int(input('Enter the sixth number of the Matrix : '))
            var7= int(input('Enter the seventh number of the Matrix : '))
            var8= int(input('Enter the eighth number of the Matrix : '))
            print()
            self._x= numpy.array(
                ([[var1,var2],[var3,var4]])
            )
            self._y= numpy.array(
                ([[var5,var6], [var7,var8]])
            )
            print('Confirm your inputs')
            print(f'x = \n{self._x}\ny = \n{self._y}')
            choice_= input('Enter y/n : ')
            if choice_ == 'n':
                break

    def main(self):
        while True:
            print('''
                1. Read two Matrices
                2. Add
                3. Subtract
                4. Multiply
                5. Divide
                6. Transpose
                7. Quit
            ''')
            try:
                choice_= int(input('Enter your choice from the given choices : '))
                while True:
                    if choice_ not in range(1,8):
                        choice_= int(input('Please choose from the given choices : '))
                        print()
                    else:
                        break

                if choice_ == 1:
                    self.read()
                elif choice_ == 2:
                    print('Addition')
                elif choice_ == 3:
                    print('Subtract')
                elif choice_ == 4:
                    print('Multiply')
                elif choice_ == 5:
                    print('Divide')
                elif choice_ == 6:
                    print('Transpose')
                else:
                    break


            except Exception as e:
                print(e)

if __name__ == '__main__':
    Matrix().main()