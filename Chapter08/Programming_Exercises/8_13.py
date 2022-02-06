''' Not Yet completed '''
# Write a program that displays a menu and its price. Take the order from the customer.
# Check if the ordered product is in the menu. In case it is not there, the 
# customer should be added in the bill.

print('--- A Program to display a menu and its price ---')
print()

class Cafe:
    def menu(self):
        """ This function displays the Cafe Menu as reference before ordering """
        print(f'{("*"*11)} Sunny Cafe Order from {("*"*11)}')
        self.name= input(' Customer Name : ')
        self.table_number= int(input('  Table Number : '))
        print()
        print(f'{("*"*11)} Sunny Cafe Menu {("*"*11)}')
        print('Food Menu:')
        print('''
            f1- Burger ($13.50)
            f2- Sandwich ($10.50)
            f3- Hotdog ($10.00)
            f4- Pasta ($12.50)
            f5- Mushroom Soup ($0.50)
        ''')
        print()
        print('Drinks Menu :')
        print('''
            d1 - Coffee ($5.90)
            d2 - Tea ($4.50)
            d3 - Juice ($6.50)
            d4 - Sky ($0.50)
            d5 - Fizzy ($2.00)
        ''')
        print()

    def Order_(self):
        ''' A function to determine the price '''
        dict_= {
            'f1': 'Burger',
            'f2': 'Sandwich',
            'f3': 'Hotdog',
            'f4': 'Pasta',
            'f5': 'Mushroom Soup'
        }
        while True:
            self.choice_= input('Order 1 : ')
            self.quantity_= input('Order quantity : ')

            print()

            cont_= input('Would you wish to continue(y/n)? ')
            if cont_ == 'y':
                break




if __name__ == '__main__' : 
    Cafe().menu()