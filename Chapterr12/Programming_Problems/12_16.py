# A program that accepts date of birth along with other personal details of a person.
# Throw an exception if an invalid date is entered

import datetime
print('--- A Program to display date of birth and personal details---')
print()


def date_validation(day, month, year):
    isValidDate = True

    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
        if (isValidDate):
            print('Yes')
        else:
            print('No')


date_validation(10, 12, 2000)
