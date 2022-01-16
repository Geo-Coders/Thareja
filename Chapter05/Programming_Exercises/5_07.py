# Write a function that accepts an integer between 1 and 12
#to represent the month number and displays the corresponding 
# month of the year (For example, if month= 1, then display JANUARY).

print('--- A Program to display the name of the Month given the number ---')
print()

def month_name (number):
    ''' A function that take a number then it returns a corresponding month '''
    dict_months= {
        1:'JANUARY',
        2:'FEBRUARY',
        3:'MARCH',
        4:'APRIL',
        5:'MAY',
        6:'JUNE',
        7:'JULY',
        8:'AUGUST',
        9:'SEPTEMBER',
        10:'OCTOBER',
        11:'NOVEMBER',
        12:'DECEMBER'
    }

    try:
        return dict_months[number]

    except (KeyError, ValueError):
        return ('Incorrect month number')


def main():
    month_number = int(input("Enter the number of the month : "))
    print("Enter the month : ", month_name(month_number))
    print()


if __name__ == '__main__':
    main()
         