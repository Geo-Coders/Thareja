# Write a program to check whether a dictionary has some key-value pairs stored in it or not

print('--- A Program to check a Dictionary ---')
print()

dict_={'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
print(('key1', 'val1') in dict_.items())
print(('key1', 'val2') in dict_.items())
print(('key1', 'val2') not in dict_.items())

print()
