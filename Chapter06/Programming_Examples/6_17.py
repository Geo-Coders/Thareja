# Write a program to print the last word of the string

import re
result= re.findall(r'\w+$', 'Good Going Python')
print(result)