# A class square that finds the square of a number
# Throw an exception if instead of the number, user enters a character

print('--- A Program to find the square of a number---')
print()


class square:
    def __init__(self, val):
        self.val = val  # int(input('Enter a number'))

        try:
            print(self.val ** 2)
        except ValueError:
            print('please enter numbers only')
