# Write a program to read month of the year as an integer. 
# Then display the name of the month


print('--- A Program to display the name of the month from the entered number of month ---')
print()
print('Enter -1 to quit the Program')

months= {
    1:'January',
    2:'February',
    3:'March',
    4:'April',
    5:'May',
    6:'June',
    7:'July',
    8:'August',
    9:'September',
    10:'October',
    11:'November',
    12:'December'
}
print()

month_number= int(input('Enter the number of the month in a year: '))
while month_number != -1:
    try:
        print(f'The month entered is {months[month_number]}')
        print()

    except (ValueError, KeyError):
        print('Invalid month number! \n\nEnter an integer number from 1 to 12')
    
    month_number= int(input('Enter the number of another month: '))

