# Write a function to reverse a string if its length is a multiple of 4

print('--- A Program that display a reverse of a string ---')
print()

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('python'))

print()

# Obtain from 'https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-20.php'


