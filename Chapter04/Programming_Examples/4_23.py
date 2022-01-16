# Write a program to enter a binary number and convert it into decimal number

binary_num= int(input('Enter the binary number: '))
decimal_num = i = 0

while binary_num != 0:
    remainder_ = binary_num % 10
    decimal_num = decimal_num + remainder_ * (2 ** i)
    binary_num = binary_num // 10
    i += 1

print(f'The decimal equivalent is {decimal_num}')


