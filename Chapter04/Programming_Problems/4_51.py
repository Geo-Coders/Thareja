# Write a simple Python program that displays the following powers of 2, 
# one per line: 2^1, 2^2, 2^3, 2^4, 2^5, 2^6, 2^7, 2^8.

print('\t\t--- A Program to display powers of 2 ---')
print()

nth_num= int(input('Enter the nth number of the powers to display: '))

print()

for i in range(1, nth_num+1):
    print(f'2^{i}')
    print()
