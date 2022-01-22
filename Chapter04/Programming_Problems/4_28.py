# Write a program that accepts the current date and the date of birth of the user. 
# Then calculate the age of the user and display it on the screen 
# Note that the date should be displayed in the format  specified as - dd/mm/yy

print('----- A program to calculate age -------')
print()

from datetime import datetime
Birth_date = int(input('Enter your date of birth (dd/mm/yy) : '))

age_in_years = datetime.now().year -Birth_date

print(age_in_years)


