# Write a program that scans an email address and forms a tuple of user name
# and domain

addr= input('Enter your email address (abc@gmail.com) : ')
user_name, domain_name= addr.split('@')

print(f'User Name : {user_name}')
print(f'Domain Name : {domain_name}')