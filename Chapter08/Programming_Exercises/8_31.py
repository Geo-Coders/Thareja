# Write a program that creates a list of numbers from 1-50 that are either divisible by 3 or divisible by 6

print('--- A Program to print all number that divisible by 3 and 5 ---')
print()


def result(N):
	
	for num in range(1,N):
		
			if num % 3 == 0 and num % 5 == 0:
				print(str(num) + " ", end = "")
				
			else:
				pass

if __name__ == "__main__":

	N = 50
	
	result(N)

