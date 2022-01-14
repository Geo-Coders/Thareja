# ----- program 4.22 -----
# Write a program to enter a decimal number. Calculate and display the binary equivalent of this number

decimal_num = int(input('Enter the decimal number : '))
binary_num = 0
i = 0
while decimal_num != 0:
    remainder = decimal_num % 2
    binary_num = binary_num +remainder * (10**i)
    decimal_num = decimal_num / 2
    i += 1
print('The binary equivalent =',binary_num)