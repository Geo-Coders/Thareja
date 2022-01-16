# Write a program to sum the series 1^2/1 + 2^2/ 2 + 3^2/3 + n^2/n
print('--- A Program to sum a series of numbers ---')
print()
print('The series is in the form of: (1^2/1) + (2^2/2) + (3^2/3) + (n^2/n)')
print()

num_= int(input('Enter the nth number of the series: '))

series_sum= 0.0
for i in range(1,(num_+1)):
    series_sum += float(i**2) / i

print(f'\nThe sum of the series is: {series_sum}')
















