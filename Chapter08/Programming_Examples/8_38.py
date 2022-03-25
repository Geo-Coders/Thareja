# Write a program that has a set of words in English language and their corresponding words in Hindi
# Define another dictionary that has a list of words in Hindi and their corresponding words in urdu
# Take all words from English language and display their meanings in both languages

E_H = {'Friend' : 'Mitr', 'Teacher' : 'Shikshak', 'Book' : 'Pustak', 'Queen' : 'Rani'}
H_U = {'Mitr' : 'Dost', 'Shikshak' : 'Adhyapak', 'Pustak' : 'Kitab', 'Rani' : 'Begum'}
for i in E_H:
    print(F'{i} in Hindi means {E_H[i]} and in Urdu means {H_U[E_H[i]]}' )