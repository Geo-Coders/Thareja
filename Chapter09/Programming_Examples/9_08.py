# Write a program that has a class store which keeps a record of code ans price of each product
# Display a menu of all products to the user and prompt him to enter the quantity of each item required
# Generate a ball and display the total amount

class store:
    _item_code = []
    _price = []
    def get_data(self):
        for i in range(5):
            self._item_code.append(int(input('Enter the code of item : ')))
            self._price.append(int(input('Enter the price : ')))
    def display_data(self):
        print('ITEM CODE \t PRICE')
        for i in range(5):
            print(self._item_code[i], '\t\t', self._price[i])
    def calculate_bill(self,quant):
        total_amount = 0
        for i in range(5):
            total_amount = total_amount + self._price[i] * quant[i]
            print('***********BILL*****************')
            print('ITEM \t PRICE \t QUANTITY \t SUBTOTAL')
            for i in range(5):
                print(self._item_code[i], '\t', self._price[i], '\t', quant[i], '\t', quant[i] * self._price[i])
                print('***************************')
                print(f'Total= {total_amount}')
s= store()
s.get_data()
s.display_data()
q = []
print('Enter the quantity of each item : ')
for i in range(5):
    q.append(int(input()))
    s.calculate_bill(q)
