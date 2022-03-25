# Write a program that creates a list of words by combining two individual lists

List_words = []
for x in ['Hello ', 'World ']:
    for y in['Python', 'Programming']:
        word = x + y
        List_words.append(word)
print(f'List combining the two individual lists is {List_words}')