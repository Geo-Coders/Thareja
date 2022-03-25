# Write a program that prints all consonants in a string using list comprehension

test = 'Hello World'
result = ''.join([(chr) for chr in test if chr not in 'a, e, i, o,u,A,E,I,O,U'])
print(result)