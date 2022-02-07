# Write a function that takes a list of words and returns the length of the longest one
print('----- A program to return longest word in a list -----')
print()

def find_longest_word(text):
    longest_word = max(text.split())
    return longest_word, len(longest_word)
text = input('Enter a list of words : ')
word = find_longest_word(text)
print(word)