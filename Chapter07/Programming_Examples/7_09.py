# Write a program that generates a Quiz and uses two files- Questions.txt
# and Answers.txt. The Program opens Questions.txt and reads a question and displays
# the question with options on the screen. The Program then opens the Answer.txt file 
# and displays the correct answers.

file1= open('Questions.txt','r')
file2= open('Answers.txt', 'r')
ques= file1.read()
qlines= ques.split('\n')

for lines in qlines:
    print(lines)

ans= file2.read()
alines= ans.split('\n')
print('CORRECT ANSWERS')

for lines in alines:
    print(lines)


