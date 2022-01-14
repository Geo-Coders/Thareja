# Write a program to enter a number and then calculate the sum of its digits

sumOfDigits= 0
num= int(input('Enter the number: '))
while num != 0:
    temp= num % 10
    sumOfDigits += temp
    num= num // 10

print(f'The sum of digits is: {sumOfDigits}')