# Write a program that calculates fib(n) using a dictionary

Dict= {0:0, 1:1}
def fib(n):
    if n not in Dict:
        val= fib(n-1) + fib(n-2)
        Dict[n]= val

    return Dict[n]

n= int(input('Enter the value of n: '))
print(f'Fib({n}) = {fib(n)}')