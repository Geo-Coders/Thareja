# A  company decides to give bonus to all its employees on Diwali. A 5% bonus on salary is given to the male workers and 10% bonus on salary to female workers.
# Write a program to enter the salay of the employees and sex of the employee. if the salary of the employee is less than $ 10,000 then the employee gets an extra 2% bonus on salary.
# Calculate the bonus that has to be given to the employee and display the salary that the employee will get.

ch= input('Enter the sex of the employee (m or F): ').lower()
sal= int(input('Enter the salary of the employee: '))

if ch == 'm':
    bonus= 0.05 * sal
bonus= 0.10 * sal

amt_to_be_paid= sal + bonus

print(f'Salary = {sal}')
print(f'Bonus = {bonus}')
print('*' * 30)
print(f'Amount to be paid: {amt_to_be_paid}')