# Write a program that displays all leap years from 1900 - 2101
print('Leap years fro 1900 - 2101 are : ')
for i in range (1900, 2101):
    if i % 4 ==0:
        print(i, end = ' ')
