# Write a program that inverts a dictionary. Thats is, it makes key of one
# dictionary value of another and vice versa.

Dict= {'Roll_No':'16/001', 'Name':'Arav', 'Course':'BTech'}
inverted= {}

for key, val in Dict.items():
    inverted[val] = key

print(f'Dict : {Dict}')
print(f'Inverted Dict : {inverted}')