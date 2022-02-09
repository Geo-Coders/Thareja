# Write a program to transpose two matrices

print('--- A Program to transpose two matrices ---')
print()

N = 4

def transpose(A,B):
	for i in range(N):
		for j in range(N):
			B[i][j] = A[j][i]

A = [ [1, 1, 1, 1],
	[2, 2, 2, 2],
	[3, 3, 3, 3],
	[4, 4, 4, 4]]


B = A[:][:]

transpose(A, B)

print("Result matrix is")
for i in range(N):
	for j in range(N):
		print(B[i][j], " ", end='')
	print()


