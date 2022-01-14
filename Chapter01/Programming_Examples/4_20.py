#----- program 4.20 -----
# Write a program to read the numbers until -1 is encountered. Find the average of positive numbers and negative numbers entered by the user

neg_count = 0
neg_s = 0
pos_count = 0
pos_s = 0
print('Enter -1 to exit...')
num = int(input('Enter the number : '))
while num != -1:
    if num < 0:
        neg_count += 1
        neg_s += num
    else:
        pos_count += 1
        pos_s += num
    num = int(input('Enter the number : '))
neg_avg = float(neg_s)/neg_count
pos_avg = float(pos_s)/pos_count
print(f'The average negative numbers is : {neg_avg}')
print(f'The average positive numbers is : {pos_avg}')
