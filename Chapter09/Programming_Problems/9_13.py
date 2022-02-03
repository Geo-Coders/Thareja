# Write a class that has a list of integers as data members and 
# read(), display(), find_largest(), find_smallest(), sum() and 
# find_mean() as its member functions.

print('--- A Program to Manipulate numbers ---')
print()

class Num:
    list0 = []
    def read(self):
        i = 0
        while i < 8:
            a = int(input('Enter the inters : '))
            Num.list0.append(a)
            i += 1

    def _find_largest(self):
        r = max(Num.list0)
        return r

    def _find_smallest(self):
        r = min(Num.list0)
        return r

    def _sum0(self):
        r = sum(Num.list0)
        return r

    def _average(self):
        _count = len(Num.list0)
        average = sum(Num.list0) / _count
        return average

    def display(self):
        print(f'The largest Number is the list is : {self._find_largest()}')
        print(f'The smallest Number is the list is : {self._find_smallest()}')
        print(f'The sum of the Numbers in the list is : {self._sum0()}')
        print(f'The mean of the Numbers in the list is : {self._average()}')

n = Num()
n.read()
n.display()


