#----- program 4.18 -----
# Write a program to calculate the sum of nmbers from m to n
from re import M


m = int(input('Enter the value of m : '))
n = int(input('Enter the value of n : '))
s = 0
while m <= n:
    s = s+m
    m += 1
print(f'SUM = {s}')
