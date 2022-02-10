# Write a function to get a string made of 4 copies of the last two characters of a specified string
# (length must be at least 2)

print('--- A Program display a string of 4 copies of last a character ---')
print()

def insert_end(str):
	sub_str = str[-2:]
	return sub_str * 4

print(insert_end('Python'))
print(insert_end('Exercises'))

print()

