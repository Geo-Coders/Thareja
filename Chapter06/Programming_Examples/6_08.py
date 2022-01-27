# Write a program that emulates the rfind function

def rfind_ch(s, c):
    index = len(s)-1
    while index >= 0:
        if s[index] == c:
            return index
        index = index - 1
    return - 1
str = input('\n Enter a string : ')
ch = input('\n Enter a character to be searched : ')
index = rfind_ch(str, ch)
if index != -1:
    print(f'{ch} is found at location {index}')
else:
    print(f'{ch} not found in the strind')
    
