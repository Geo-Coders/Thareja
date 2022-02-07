# Write a program to count the occurrence of each word in a given sentence
def count_word(sentence, word):
    count = 0
    for i in sentence:
        if i == word:
            count+=1
    return count
sentence = input('Enter a sentence : ') 
word = input('Enter the word to be searched : ')
count = count_word(sentence, word)
print(count)
