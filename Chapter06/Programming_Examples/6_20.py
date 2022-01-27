# Write a program to extract a date from a given string

import re
result = re.findall(r'\d{2}-\d{2}-\d{4}', 'Hello my name is Srishti and my date of joining is 11-15-1999 and have experience of more than 17 years')
print(f'Date of appointment is : {result}')