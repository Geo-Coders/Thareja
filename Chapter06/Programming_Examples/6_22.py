# Write a program that prints only those words that starts with a vowel

import re
result = re.findall(r'\b[aeiouAEIOU]\w+', 'Hello my name is Srishti and my date of joining is 11-15-1999 and have experience of more than 17 years')
print(result)