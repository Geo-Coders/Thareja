# Write a program that replaces,,;,-from a string with a blank space character
import re
result = re.sub(r'[;,-]', ' ', 'Hello! my name- is Srishti.; and my date-of-joining is 11-15-1999 and have experience of, more than 17 years;')
print(result)