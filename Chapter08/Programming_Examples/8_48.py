# Write a program that combines the lists to a dictionary

keys = ['Name', 'Age', 'Marital status']
values = ['om', 38, 'Married']
details = zip(keys, values)
Dict = dict(details)
print(Dict)