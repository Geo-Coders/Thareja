# Write a program to sum the series- 1/1 + 2**2/2 + 3**3/3 +....+n**n/n

n = int(input('Enter the value of n : '))
s = 0.0
for i in range(1, n+1):
    a = float(i**i)/i
    s = s + a
print(f'The sum of the series is {s}')