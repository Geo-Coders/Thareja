# Write a program that prompts the user to enter a message. 
# Now count and print the number of occurrences of each character.

from email import message


def count(message):
    letter_counts= {}
    for letter in message:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    print(letter_counts)

message= input('Enter a message : ')
count(message)