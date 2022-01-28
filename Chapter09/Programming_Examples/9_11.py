# Write a program that uses datetime module within a class. Enter manufacturing date and expiry date of the product. 
# The program must diplay the years, months and days that are left for expiry.

import datetime

class Product:
    def __init__(self):
        self.manufacture= datetime.datetime.strptime(input('Enter manufacturing date (mm/dd/yyyy): '), '%m/%d/%Y')
        self.expiry= datetime.datetime.strptime(input('Enter expiry date (mm/dd/yyyy): '), '%m/%d/%Y')

    def time_to_expire(self):
        today= datetime.datetime.now()
        if (today > self.expiry):
            print('Product has already expired.')
        else:
            time_left= self.expiry.date() - datetime.datetime.now().date()
            print(f'Time left : {time_left}')

x= Product()
x.time_to_expire()