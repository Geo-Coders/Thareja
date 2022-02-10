# Write a program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form(alphanumerically).

print('--- A Program to Display the Unique words in sorted form ---')
print()

items = input('Input comma separated sequence of words : ')
words = [word for word in items.split(',')]
print()
print('The Words in alphanumerical order : ')
print(','.join(sorted(list(set(words)))))

print()