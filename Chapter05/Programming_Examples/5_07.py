# Write a program to calculate simple interest. Suppose the customer is a 
# senior citizen. He is being offered 12% rate of interest,
# for all other customers,the ROI is 10%.

def interest(principle, num_of_years, is_senior_citizen):
    if is_senior_citizen.lower() == 'y':
        simple_interest= float((principle * num_of_years *12)/100)

    else:
        simple_interest= float((principle * num_of_years *10)/100)

    return simple_interest

principle_= float(input('Enter the principle amount: '))
num_of_years_= float(input('Enter the number of years: '))
Is_senior_citizen= input('Is customer a senior citizen(y/n): ')

print()

print(f'Interest : {round(interest(principle_, num_of_years_, Is_senior_citizen),2)}')
