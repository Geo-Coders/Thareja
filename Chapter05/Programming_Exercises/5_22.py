# Write a program using the function (C(n,r)) 
# To calculate the compound interest for the given principal, rate of interest and number of years
print('----- A program to compute compound interst -----')
print()
def compound_interest(Principle, time, rate):
    ''' To calculate compound interest'''
    Amount = Principle * (1 + rate/100)** time
    compound_interest = Amount- Principle
    print(f'Compound interest is {compound_interest}')
compound_interest(20000, 2, 15)

