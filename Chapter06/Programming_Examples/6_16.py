# Write a program to print the first word of the string

import re
result = re.findall(r'^\w+', 'Going Good Python')
print(result)