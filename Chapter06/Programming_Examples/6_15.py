# Write a program to extract each word from a string using a regular expression

import re
result= re.findall(r'\w+', 'Good Going Python')
print(result)