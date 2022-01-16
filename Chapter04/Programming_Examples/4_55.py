# Write a program that prompts users to enter numbers. The process will repeat until user enters -1. 
# Finally, the program prints the count of prime and composite numbers entered.

print('Enter -1 to quit')

prime_count= 0
comp_count= 0

n= int(input('Enter the number: '))
while n != -1:
    flag= 0
    for i in range(2,n):
        if n % i == 0:
            flag= 1
            break

    if flag == 0:
        prime_count += 1
    
    else:
        comp_count += 1

    n= int(input('Enter the number: '))

print(f'Number of prime numbers is : {prime_count}')
print(f'Number of composite numbers is : {comp_count}')

