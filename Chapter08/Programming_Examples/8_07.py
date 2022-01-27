# Write a program that forms a list of first character of every word in another list.
list1= ['Hello', 'Welcome', 'To', 'The', 'World', 'of', 'Python']
letters= []

for word in list1:
    letters.append(word[0])

print(letters)

