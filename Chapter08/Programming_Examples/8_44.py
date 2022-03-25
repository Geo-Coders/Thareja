# Write a program that has a dictionary of names of students and a list of their marks in 4 subject
# Create another dictionary from this dictionary that has name of the students and their total marks
# Find out the topper and his/her score

Marks = {'Neha': [97,89,94,90], 'Mitul' : [92,91,94,87], 'Shefali': [67,99,88,90]}
tot = 0
Tot_Marks = Marks.copy()
for key, val in Marks.items():
    tot = sum(val)
    Tot_Marks[key] = tot
print(Tot_Marks)
max = 0
Topper = ''
for key, val in Tot_Marks.items():
    if val >max:
        max = val
        Topper = key
print(f'Topper is : {Topper} with marks = {max}')
        
        