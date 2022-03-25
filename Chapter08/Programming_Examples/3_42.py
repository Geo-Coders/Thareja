# Write a proram to store a sparse matrix as a dictionary
matrix = [[0,0,0,1,0],
          [2,0,0,0,3],
          [0,0,0,4,0]]
Dict = {}
print('sparse matrix')
for i in range(len(matrix)):
    print('\n')
    for j in range(len(matrix[i])):
        print(matrix[i][j], end = ' ')
        if matrix[i][j] !=0:
            Dict[(i,j)] = matrix[i][j]
print('\n\nSparse Matrix can be efficiently represented as Dictionary : ')
print(Dict)