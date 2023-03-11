# Write a program to make a quiz. Use zip() function to extract question
# into and answer into two separate lists.

print('---- A Program to implement zip() function ---')
print()

questions= [
    'What is your Name? ',
    'How old are you? ',
    'Which country are you from? '
]

answers= [
    'Jamal Makame',
    '26 years old',
    'Tanzania'
]

for i, (question, answer) in enumerate(zip(questions, answers)):
    print((i+1), question, answer)

print()

