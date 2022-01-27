# Write a function is_leap_year which takes the year as its argument 
# And checks whether the year is a leap year or not and then displays an appropriate message on the screen
print('--------- A program to identify a Leap year--------')
print()

def is_leap_year(year):
    if year % 4==0:
        return 1
    else:
        return 0
year = int(input('Enter the year : '))
flag = is_leap_year(year)
if flag == 1:
    print('is a leap year')
if flag == 0:
    print('Is not a leap year')
