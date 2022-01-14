# ----- program 4.14 -----
# Write a program to enter the marks of a student in four subjects. Then calculate the total and aggregate, and display the garde obtained by the student. If the student scores an aggregate greater than 755, then the grade is Distinction. If aggregate is 60>= and < 75, then  the grade is First Division. If aggregate is 5o>= and <60, then the grade is Second Division. If aggregate is 40>= and<50, then the grade is Third Division. Else the grade is Fail
marks1 = int(input('Enter the marks in Mathematics : ')) 
marks2 = int(input('Enter the marks in Science : ')) 
marks3 = int(input('Enter the marks in Social Science : ')) 
marks4 = int(input('Enter the marks in Computers : ')) 

total = marks1 + marks2 + marks3 + marks4
avg = float(total)/4
print(f'Total = {total}' f'\t Aggregate = {avg}')
if avg >=75:
    print('Distinction')
elif avg >=60 and avg <75:
    print('First Division')
elif avg >=50 and avg <60:
    print('Second Division')
elif avg >=40 and avg <50:
    print('Third Division')
else:
    print('Fail')
