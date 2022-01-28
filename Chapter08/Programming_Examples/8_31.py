# Write a program that generates a set of prime numbers and 
# another set of odd numbers. Demonstrate the result of union, 
# intersection, difference and symmetric difference operations 
# on these sets.

odds= set([x*2+1 for x in range(1,10)])

print(odds)

primes= set()
for i in range(2,20):
    j= 2
    flag= 0
    while j<(i/2):
        if i%j == 0:
            flag= 1
        j += 1

    if flag == 0:
        primes.add(i)

print(primes)
print(f'UNION : {odds.union(primes)}')
print(f'INTERSECTION : {odds.intersection(primes)}')
print(f'SYMMETRIC DIFFERENCE : {odds.symmetric_difference(primes)}')
print(f'DIFFERENCE : {odds.difference(primes)}')

