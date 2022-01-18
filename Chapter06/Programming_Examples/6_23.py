# Write a program that validates a mobile phone number. The number should start with 7, 8 or 9 followed by 9 digits.

import re

List= ['7838456789', '1234567890', '9876543210', '8901234567', '4567890123']

for i in List:
    result= re.findall(r'[7-9]{1}[0-9]{9}', i)
    if result:
        print(result, end=' ')
        