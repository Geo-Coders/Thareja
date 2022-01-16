# Write a program to calculate sum of cubes of numbers from 1-n
n= int(input('Enter the value of n: '))
s= 0
for i in range(1, n+1):
    a= i**3
    s += a

print(f'The sum of cubes is {s}')