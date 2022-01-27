# Write a program the defines a list of countries that are a member of BRICS.
# Check whether a country is a member of BRICS or not

country= ['Brazil', 'India', 'China', 'Russia', 'Sri Lanka']
is_member= input('Enter the name of country: ')
if is_member in country:
    print(f'{is_member} has also joined BRICS')
else:
    print(f'{is_member} is not a member of BRICS')