# Write a program to sum the series- 1 + 1/2 + ... + 1/n

n= int(input('Enter the number: '))
s= 0.0

for i in range(1, n+1):
    a= 1.0 // i
    s += a

print(f'The sum of 1, 1/2,..., 1/{n} is {s}')