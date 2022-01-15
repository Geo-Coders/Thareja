# Write a program that displays all the numbers from 1-100 
# that are not divisible by 2 as well as by 3.

print('--- A Program to display a list of number that are not divisible by 2 and 3 ---')
print()

for num in range(0,101):
    if (num % 3 != 0) and (num % 2 != 0):
        print(f"{num}", end=' ')

print()