# Write a program to print the sum of all odd numbers from 1 to 100
print('------ A program to print the sum of odd numbers from 1 to 100 -----')
print()

sum = 0
for i in range(0, 101):
    if i % 2 != 0 :
     sum = sum+i
   
print(f'The sum of all odd numbers from 1 to 100 is {sum}')