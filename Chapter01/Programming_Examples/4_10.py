#----- program 4.10 -----
# Write a program to find the greatest number from three numbers
num1 = int(input('Enter the first number : '))
num2 = int(input('Enter the second number : '))
num3 = int(input('Enter the third number : '))
if num1 > num2:
    if num1 > num3:
        print(num1,'is greater than', num2, 'and', num3)
    else:
        print(num3,'is greater than', num1, 'and', num2)
elif num2 > num3:
     print(num2,'is greater than', num1, 'and', num3)
else:
    print('The three numbers are equal')
        