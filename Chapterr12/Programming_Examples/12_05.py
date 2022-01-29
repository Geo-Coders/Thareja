# Write a number game program. Ask the user to enter a number.
# if the number is greater than number to be guessed, raise a
#  ValueTooLarge exception and prompt the user to enter again. 
# Quit the program only when the user enters the correct number.

class ValueTooSmallError(Exception):
    def display(self):
        print('Input value is too small')

class ValueTooLargeError(Exception):
    def display(self):
        print('Input value is too large')

max= 100
while 1:
    try:
        num= int(input('Enter a number : '))
        if num == max:
            print('Great you succeeded...')
            break
        if num < max:
            raise ValueTooSmallError
        elif num > max:
            raise ValueTooLargeError

    except ValueTooSmallError as s:
        s.display()

    except ValueTooLargeError as l:
        l.display()
