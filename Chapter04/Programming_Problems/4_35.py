# Write a program that prints whether every number in a range is prime or composite

print('--- A Program to check whether a number is prime or composite ---')
print()

num = int(input('Enter a number: '))
print()
# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(f'{num} is a composite number')
           print(f'{i} times {num//i} is {num}')
           print()
           break
   else:
       print(f'{num} is a prime number')
       print()
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(f'{num} is not a prime number')
 