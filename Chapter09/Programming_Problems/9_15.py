# Write a program that swaps two members of a class

print('--- A Program tha swaps two members of a class ---')
print()

class Swapper:
    def __init__(self):
        self.var1= input('Enter the first input to swamp : ')
        self.var2= input('Enter the second input to swamp : ')

    def swampper(self):
        print(f'Before swapping {self.var1} and {self.var2}')

        Temp= self.var1
        self.var1= self.var2
        self.var2= Temp

        print(f'After swapping {self.var1} and {self.var2}')
        

test= Swapper()
test.swampper()