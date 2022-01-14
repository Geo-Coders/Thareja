# Write a program using for loop to calculate the average of first n natural numbers
n= int(input('Ente the value of n: '))
avg= 0.0
s= 0
for i in range(1, n+1):
    s += i

avg= s / i

print(f'The sum of first {n} natural numbers is {s}')
print(f'The average of first {n} natural numbers is {avg}')