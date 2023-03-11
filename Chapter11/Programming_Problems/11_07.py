# Write a menu driven program to overload +=, -=, ==, >= and
# <= operators on the Distance class

print('--- Operator Overloading on Distance Class ---')
print()


class Distance:
    def __init__(self, m):
        self.m = m

    def __isub__(self, other):
        self.m -= other.m
        return self.m

    def __iadd__(self, other):
        self.m += other.m
        return self.m

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.m == other.m
        return False

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.m >= other.m
        return False

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.m <= other.m
        return False


print('Enter Your choice from the given Menu to quit the Program Enter \'quit\'')
while True:
    print('1. <= Addition =>')
    print('2. <= Subtraction =>')
    print('3. <= Equating two inputs =>')
    print('4. <= Less Than =>')
    print('5. <= Greater Than =>')

    choice_ = (input('Choose a number from the given options above : '))

    while True:
        if choice_.lower() not in ['1', '2', '3', '4', '5', 'quit']:
            choice_ = (input('Invalid Input, Please Choose a valid Number : '))
            print()
        else:
            break

    if choice_ == '1':
        print()
        print('--- Addition Option has been selected ---')
        print()
        test0 = int(input('Enter the first distance : '))
        var1 = Distance(test0)
        test1 = int(input('Enter the second Distance : '))
        var2 = Distance(test1)
        var1 += var2
        print(f'The answer is : {var1}')

    elif choice_ == '2':
        print()
        print('--- Subtraction Option has been selected ---')
        print()
        test0 = int(input('Enter the first distance : '))
        var1 = Distance(test0)
        test1 = int(input('Enter the second Distance : '))
        var2 = Distance(test1)
        var1 -= var2
        print(f'The answer is : {var1}')

    elif choice_ == '3':
        print()
        print('--- Equating Option has been selected ---')
        print()
        test0 = int(input('Enter the first distance : '))
        var1 = Distance(test0)
        test1 = int(input('Enter the second Distance : '))
        var2 = Distance(test1)
        if var1 == var2:
            print(f'{test0} is equal to {test1}')
        else:
            print(f'{test0} is not equal to {test1}')

    elif choice_ == '4':
        print()
        print('--- Less than or Equal to  Option has been selected ---')
        print()
        test0 = int(input('Enter the first distance : '))
        var1 = Distance(test0)
        test1 = int(input('Enter the second Distance : '))
        var2 = Distance(test1)
        print()
        if var1 <= var2:
            print(f'{test0} is less than or equal to {test1}')
        else:
            print(f'{test0} is not less than or equal to {test1}')

    elif choice_ == '5':
        print()
        print('--- Greater than or Equal to  Option has been selected ---')
        print()
        test0 = int(input('Enter the first distance : '))
        var1 = Distance(test0)
        test1 = int(input('Enter the second Distance : '))
        var2 = Distance(test1)
        print()
        if var1 >= var2:
            print(f'{test0} is greater than or equal to {test1}')
        else:
            print(f'{test0} is not greater than or equal to {test1}')
    else:
        print('Quiting the Program')
        break

    print()
