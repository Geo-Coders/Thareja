# Write a program that uses a regular expression to match strings which
# starts with a sequence of digits (at least one digit) followed by a blank and after this 
# arbitrary characters.

import re
pattern= r'^[0-9]+ .*'
string= '12 abc'
match= re.search(pattern, string)

if match:
    print('Match')