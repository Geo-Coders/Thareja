# rite a program that displays information about an employee 
# Use nested dictionary to do that task

employees = {'James' :{'Gender' : 'male', 'Age' : 51}, 'Ann': {'GEnder' : 'Female', 'Age': 30}}
for key, val in employees.items():
    print(key, val)