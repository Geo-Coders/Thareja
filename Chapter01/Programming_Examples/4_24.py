#------ program 4.24 -----
# Write a program to read a character until a * is encountered. Also count the number of uppercase, lowercase, and numbers entered by the users

num_count = 0
up_count = 0
low_count = 0

while ch != '*':
    ch = input('Enter any character : ')
    if ch.isdigit():
        num_count += 1
    elif ch.islower():
        low_count += 1
    elif ch.isupper():
        up_count += 1

print(f'Number of lowercase character are : {low_count}')
print(f'Number of uppercase character are : {up_count}')
print(f'Number of numerals are : {num_count}')
