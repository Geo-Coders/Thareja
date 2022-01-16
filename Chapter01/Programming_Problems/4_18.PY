# Write a program to read a floating point number and an integer
# If the value of the floating point number is greater than 4.14 then add 10 to the integer

num1 = float(input('Enter a floating number : '))
num2 = int(input('Enter an integer : '))
if num1 > 4.14:
    num2 = num2 + 10
    print(num2)
else:
    print(num2)

