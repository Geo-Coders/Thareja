# Write a function that accepts two positive numbers n and m. 
#  where m  <= n and returns numbers between 1 and n that are divisible by m
print('------ A program to return numbers divisible  ------')
print()

def divisible(n,m):
    for i in range (1,n):
        if i % m == 0:
            print(i)
    
               
n = int(input('Enter the value of n : '))
m = int(input('Enter the value of m : '))
i = divisible(n, m)


    