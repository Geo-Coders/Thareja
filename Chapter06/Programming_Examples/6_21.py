# Write a program to extract the year from a given string

import re

string= 'Hello, my name is Jamal and my date of \
    joining is 11-15-1999 and have experience of more than 17 years'
pattern= r'\d{2}-\d{2}-(\d{4})'

result= re.findall(pattern, string)

print(f'Year of joining is : {result}')