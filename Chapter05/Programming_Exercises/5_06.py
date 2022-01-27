# Write a function is_prime() that returns a 1 if the argument passed to it is a prime number and a 0 otherwise
print('----- This program to check whether the argument is a prime number or not-----')
print()


def is_prime(num):
    for i in range(2, num):
    
        if  num % i ==0:
            return 0
        else:
            return 0
    return 1
num = int(input('Enter the number : '))
flag = is_prime(num)
if flag ==1:
    print('The number is prime')
if flag == 0:
    print('The number is not prime')

    
    