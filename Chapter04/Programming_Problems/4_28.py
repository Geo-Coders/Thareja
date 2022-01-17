# Write a program that accepts the current date and the date of birth of the user. 
# Then calculate the age of the user and display it on the screen 
# Note that the date should be displayed in the format  specified as - dd/mm/yy

Todays_date = int(input('Enter today\'s date (mm/dd/yy): '))
Birth_date = int(input('Enter your date of birth (dd/mm/yy) : '))

if Todays_date < Birth_date:
     print('Enter a valid date')
else:
    age =  Todays_date - Birth_date
    print(f'Your age is {age}')

