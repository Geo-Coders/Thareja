# An employee's total weekly pay is calculated by multiplying the hourly wage and number of regular hours plus overtime pay
# which in turn is calculated as total overtime hours multiplied by 1.5 times the hourly wage
# Write a program that takes as inputs the hourly wage
# Total regular hours and total overtime hours
# and prints an employee's total weekly pay
print('---- A program to calculate employees weekly wages -----')
print()

Hourly_wage = int(input('Enter the hourly wage amount : '))
Total_regular_hours = int(input('Enter the total regular hours worked : '))
Total_Overtime_hours = int(input('Enter the total overtime hours : '))

Overtime_pay = Total_Overtime_hours * (1.5 * Hourly_wage) 
Weekly_pay = (Hourly_wage * Total_regular_hours) + Overtime_pay


print(f'Total employee\'s wage is {Weekly_pay}')
