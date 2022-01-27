# Write a function that accepts a number n as input 
# and returns the average of numbers from 1 to n 
print('----- A program to average numbers from 1 to n ------')
print()
def average(n):
    sum = 0
     
    for i in range(1, n+1):
        sum = sum + i
        average = sum/i
    return average

n = int(input('Enter a number: '))
result = average(n)
print(f'The average of numbers from 1 to {n} is {result} ')
        