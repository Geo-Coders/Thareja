# Write a program to count number of times a recursive function is called.

def func(n, count=0):
    if n==0:
        return count

    else:
        return func(n-1, count+1)

print(f'Number of times resursive function was invoked = {func(500)}')