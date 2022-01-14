#------ program 4.24 -----
# Write a program to read a character untill a * is encountered. Also count the number of uppercase, lowercase, and numbers entered by the users

ch = input('Enter any character : ')
num_count = 0
up_count = 0
low_count = 0
if ch >= '0' and ch <= '9':
    num += 1
elif ch>= 'a' and ch <= 'z':
    low_count += 1
elif ch >= 'A' and ch <= 'Z':
    up_count += 1
while ch != '*':
    ch = input('Enter any character : ')
    if ch >= '0' and ch <= '9':
        num_count += 1
    elif ch >='a' and ch <= 'z':
        low_count +=1
    elif ch >= 'A' and ch <= 'Z':
        up_count += 1
print(f'Number of lowercase character are : {low_count}')
print('Number of uppercase character are : ',up_count)
print('Number of numerals are : ',num_count)