# Write a program with class Bill
# The users have the option to pay the bill either by cheque or by cash
# Use the inheritance to model this situation

from multiprocessing.sharedctypes import Value


class Bill:
    def __init__(self,items,price):
        self.total = 0
        self.items = items
        self.price = price
        for i in self.price:
            self.total +=1
    
    def display(self):
        print('\n ITEM \t\t\t PRICE')
        for i in range(len(self.items)):
            print(self.items[i], '\t', self.price[i])
            print('*************')
            print(f'Total = {self.total}')
            
class Cash_Payment(Bill):
    def __init__(self, items, price, deno, value):
        Bill.__init__(self, items, price)
        #self.n = n;
        self.deno = deno
        self.value = Value
    def show_Cash_Payment_Details(self):
        Bill.display(self)
        for i in range(len(deno)):
            print(deno[i], '*', value[i], '=', deno[i]*value[i])
            
class Cheque_Payment(Bill):
    def __init__(self, items, price, cno, name):
        Bill.__init__(self, items, price)
        self.cno = cno
        self.name = name
    def show_Check_payment_Details(self):
        Bill.display(self)
        print(f'CHEQUE NUMBER : {self.cno}')
        print(f'BANK NAME : {self.name}')
        
items = ['External Hard Disk', 'RAM', 'Printer', 'PenDrive']
price = [5000, 2000, 6000, 800]
option = int(input('would you like to pay by cheque or cash(1/2) : '))
if option ==1:
    name = input('Enter the name of the bank : ')
    cno = input('Enter the cheque number : ')
    cheque = Cheque_Payment(tems, price, cno, name)
    cheque.show_Check_payment_Details()
else:
    deno = [10,20,50,100,500,2000] 
    value = [1,1,1,20,4,5]
    CP = Cash_Payment(items,price, deno, value)
    CP.show_Cash_Payment_Details() 
        