# Write a program that uses a regular expression to pluralize a word

import re

def pluralize(noun):
    if re.search('[sxz]$', noun):
        return re.sub('$', 'es', noun)
    
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)

    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)

    else:
        return noun + 's'

List= ['bush', 'fox', 'toy', 'cap']
for i in List:
    print(f'{i} - {pluralize(i)}')