# Write a program that counts the number of tabs,spaces, and newline
# characters in a file

with open(input('Enter the filename: ')) as file:
    text= file.read()
    count_tab= 0
    count_space= 0
    count_nl= 0

    for char in text:
        if char == '\t':
            count_tab += 1
        if char == ' ':
            count_space += 1
        if char == '\n':
            count_nl += 1

print(f'TABS = {count_tab}')
print(f'SPCES = {count_space}')
print(f'NEW LINES = {count_nl}')