# Write a Python program to get a string made of the first 2 and the last 2
# characters from a given a string. if the string length is less than 2, return
# instead the empty string.

print('--- A Program to get a string made of first 2 and last 2 from a given string ---')
print()

s= input('Enter a string : ')
if len(s) < 2:
    print('The String must be of more than 4 characters')
else:
    ns= s[:2] + s[-2:]
    print(ns)