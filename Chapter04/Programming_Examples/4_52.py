# Write a program to print the following pattern

'''

       1
     1 2 1
   1 2 3 2 1
 1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1

'''

N = 5
for i in range(1, N+1):
    for k in range(N, i, -1):
        print(' ', end=' ')
    for j in range(1, i+1):
        print(j, end=' ')
    for l in range(i-1, 0, -1):
        print(l, end=' ')
    print()