# Write a program that print a histogram of frequencies of characters
# occurring in a message

from typing import Dict


msg= 'Hell All, Good Morning... Welcome to the World of Python'
msg= msg.lower()

Dict= dict()
for word in msg:
    if word not in Dict:
        Dict[word] = 1
    else:
        Dict[word]= Dict[word] + 1

print(Dict)

for key, val in Dict.items():
    print(f'{key} \t {"*" * val}')