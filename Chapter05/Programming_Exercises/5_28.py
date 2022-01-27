# Write a program to print Fibonacci series using recursion
print('------ A program to print Fibonacci series using recursion ------')
print()
def fibonacci(n):
    if n < 2:
        return 1
    return (fibonacci(n-1) + fibonacci(n-2)) 
n = int(input('Enter the number of terms : '))
for i in range(n):
    print('fibonacci(',i,') =', fibonacci(i))
    