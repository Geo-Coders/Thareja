# Write a program that computes P(n,r)
# Hint P- Permutation

def fact(n):
    f= 1
    if n == 0 or n == 1:
        return 1

    else:
        for i in range(1, int(n+1)):
            f *= i

    return f  

n= eval(input('Enter the value of n: '))
r= eval(input('Enter the value of r: '))

print()

result= float(fact(n))/float(fact(r))
print(f'P( {n}/{r} ) = {result}')