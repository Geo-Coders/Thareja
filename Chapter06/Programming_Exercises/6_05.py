# Write a Python program to get a single string from two given 
# separated by a space and swap the first two characters of each string

print('--- A Program to get a single string from given strings ---')
print()

string1 = input('Enter the first string : ') 
string2 = input('Enter the second string : ')

x = string2[:2] + string1[2:]
y = string1[:2] + string2[2:]

res = f'{x}_{y}'
print()
print(res)
print()