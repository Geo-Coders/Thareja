# Write a program to read the numbers untill -1 is encountered. Also count the negative, positives, and zeroes entered by the user.

neg = pos = zeroes = 0

print('Enter -1 to exit..')
while 1:
    num= int(input('Enter any number: '))
    if num == -1:
        break
    if num == 0:
        zeroes += 1
    elif num > 0:
        pos += 1
    else:
        neg += 1

print(f'Count of positive numbers entered: {pos}')
print(f'Count of negative numbers entered: {neg}')
print(f'Count of zeroes entered: {zeroes}')

    
















