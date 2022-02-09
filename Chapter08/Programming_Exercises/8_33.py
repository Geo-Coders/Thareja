# Write a program to create a list of numbers in the range 1 to 20. 
# Then delete all the numbers from the list that are divisible by 3.

print('--- A Program to implement a delete operator ---')
print()

Num = list(range(1,21))

print(f'The list of numbers from 1 to 10 = {Num}')
for index, i in enumerate(Num):
	if(i%2==0):
		del Num[index]
print(f'The list after deleting even numbers = {Num}')

print()