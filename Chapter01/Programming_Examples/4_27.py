# Write a program to print the reverse of a number

num= int(input('Enter the number: '))
print('The reversed number is: ')
while num != 0:
    temp= num % 10
    print(temp, end='')
    num= num // 10