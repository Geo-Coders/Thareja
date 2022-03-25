# write a progam that creates two sets.
# One of even number in range 1-10 and the other has all composite numbers in range 1-20
# Demostrate the use all(), issuperset(), len(), and sum() functions on the sets

evens = set([x*2 for x in range(1,10)])
print(f'EVENS : {evens}')
composites = set()
for i in range(2,20):
    j =2
    flag = 0
    while j<= i/2:
        if i% j ==0:
            composites.add(i)
        j +=1
print(f'COMPOSITES : {composites}')
print(f'SUPERSET : {evens.issuperset(composites)}')
print(f'ALL : {all(evens)}')
print(f'LENGTH OF COMPOSITES SET : {len(composites)}')
print(f'SUM OF ALL NUMBERS IN EVENS SET : {sum(evens)}')



