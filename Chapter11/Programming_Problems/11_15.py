# Write a Program to convert minutes into class Time with data members--
# hrs and mins

print('--- A Program to Convert Minutes into hrs and mins ---')
print()


class Time:
    def __init__(self, min):
        self.min= min
        self.hrs= 0

    def _convert(self):
        self.hrs = self.min // 60
        self.min %= 60

    def __str__(self):
        self._convert()
        return f'{self.hrs} hrs:{self.min} min'


input_= int(input('Enter the minutes to convert : '))
test= Time(input_)

print()

print(f'The Converted Unites are : {test}')


