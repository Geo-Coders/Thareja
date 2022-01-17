# Write a program to print the sum of all odd numbers from 1 to 100

sum = 0
for i in range(0, 101):
    if i % 2 != 0 :
     sum = sum+i
   
print(f'The sum of all odd numbers from 1 to 100 is {sum}')