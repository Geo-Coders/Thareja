# Write a program to sum the series -- 1/2 + 2/3 + ... + n/(n+1)

n= int(input('Enter the number: '))
s= 0.0

for i in range(1, n+1):
    a= float(i) / (i + 1)
    s += a

print(f'The sum of 1/2 + 2/3...n/(n+1) is {round(s,2)}')
