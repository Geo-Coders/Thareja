#----- program 4.12 -----
# Write a program to calculate tax given the following conditions
#if taxable income is 150,001 - 300,000 then charge 10% tax
#if taxable income is 300,001 - 500,000 then charge 20% tax
#if taxable income is above 500,001 then charge 30% tax
MIN1 = 1500001
MAX1 = 300000
RATE1 = 0.10
MIN2 = 300001
MAX2 = 500000
RATE2 = 0.20
MIN3 = 500001
RATE3 = 0.30

income = int(input('Enter the income : '))
taxable_income = income - 150000
if taxable_income <= 0:
    print('no tax')
elif taxable_income >= MIN1 and taxable_income < MAX1:
    tax = (taxable_income - MIN1) * RATE1
elif taxable_income >= MIN2 and taxable_income < MAX2:
    tax = (taxable_income - MIN2) * RATE2
else:
    tax = (taxable_income - MIN3) * RATE3
print('TAX = ',tax)