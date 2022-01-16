# Write a program that finds average of first n numbers using for loop

n = int(input('Enter the value of n : '))
avg = 0.0
sum = 0

for i in range(1, n+1):
    sum = sum + i
    avg = sum/n
print(f'The average of the first {n} natural numbers is {avg}')
    

