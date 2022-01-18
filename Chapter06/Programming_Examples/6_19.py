# Write a program to print only the first two characters of every word

import re

result= re.findall(r'\b\w\w', 'Good Going Python')

print(result)