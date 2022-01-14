# Write a program using for loop to calculate the value of an investment.
# input an initial value of investment and annual interest, and calculate the value of investment over time

initVal= float(input('Enter the initial value: '))
ROI= float(input('Enter the rate of interest: '))
yrs= int(input('Enter the number of years for which investment has to be done: '))

futureVal= initVal
print('\tYear \t\tValue')
print('-' * 40)

for i in range(1, yrs + 1):
    futureVal *= (1 + ROI/100.0)
    print(f'{i} \t\t {futureVal}')