# Write a program to find whether a given year is leap year or not

print('--- A Program to evaluate a year is a Leap year ---')
print()
print('Enter -1 to quit the Program')

year_to_determine= int(input('Enter the Year to determine whether is a Leap Year: '))
while year_to_determine != -1:
    while True:   
        if len(str(year_to_determine)) != 4:
            year_to_determine= int(input('Enter the correct year format(1996|2000): '))
            print()
        else:
            break

    if((year_to_determine % 400 == 0) or
    (year_to_determine % 100 != 0) and
    (year_to_determine % 4 == 0)):
        print(f'{year_to_determine} is a leap year')
    else:
        print(f'{year_to_determine} is not a leap year')

    year_to_determine= int(input('Enter another Year : ')) 
     

