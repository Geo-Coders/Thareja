# Write a Program in which an exception raised by one 
# function is handled by another function.

print('--- A Program to display Exception handler by another function ---')
print()

class InvalidAge(Exception):
    def display(self):
        print('Invalid Age entered...!')

class InvalidName(Exception):
    def display(self):
        print('Invalid Name entered...!')


try:
    name = input('Enter Your name : ')
    if len(name) == 0:
        raise InvalidName

    age = int(input('Enter Your Age : '))
    if age < 18:
        raise InvalidAge

except InvalidName as n:
    n.display()

except InvalidAge as a:
    a.display()

print()