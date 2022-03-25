# Write a program that has two sequences
# First which stores some questions and corresponding answers
# Use the zip() function to form a valid question answer series

Ques = ['Roll_No', 'Name', 'Course']
Ans = [7, 'Saesha','BSc']
for q,a in zip(Ques, Ans):
    print(f'What is your {q}?')
    print(f'My {q} is : {a}') 
