# Write a program to sum the series 1/1! + 4/2! + 27/3!+..
def fact(n):
    f = 1
    if n==0 or n==1:
        return 1
    else:
        for i in range(1, int(n+1)):
            f = f*i
    return f
n = int(input('Enter the value of n : '))
sum = 0.0
for i in range(1,n+1):
    sum = sum + (float(i**i)/fact(i))
print(f'Result : {sum}')