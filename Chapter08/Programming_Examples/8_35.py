# Write a program that has a dictionary of states and their codes.
# Add another state in the pre-defined dictionary, print all the items
# in the dictionary, and try to print code for a state that does not exist.
# Set a default value prior to printing.

states= {'Delhi' : 'DL', 'Haryana' : 'HR', 'Maharashtra': 'MH', 'Rajasthan' : 'RJ'}
states['Tamil Nadu'] = 'TN' # add another state
states.setdefault('Karnataka', 'Sorry, no idea')

print(f'Code for Rajasthan is : {states["Rajasthan"]}')
print(f'{"-"*5} CODES {"-"*5}')

for i in states.items():
    print(i)

print(f'Code for karnataka : {states.get("Karnataka")}')
