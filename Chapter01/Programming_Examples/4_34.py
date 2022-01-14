# Write a program using while loop to read the numbers untill -1 is encounteres. Also, count the number of prime numbers and composite numbers encountered by the user

total_prime = 0
total_composite = 0

while 1:
    num = int(input('Enter no : '))
    if num == -1:
        break
    is_composite = 0
    for i in range(2, num):
        if num % i == 0:
            is_composite = 1
            break
    if is_composite:
        total_composite += 1
    else:
        total_prime += 1
print(f'total composite {total_composite}')
print(f'total prime {total_prime}')
            
            
