# Write a program to print the following pattern
#     1 
#    2 2 
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5

N= 5
for i in range(1, N+1):
    for _ in range(N, i, -1):
        print('', end=' ')
    for _ in range(1, i+1):
        print(i, end=' ')
    print()