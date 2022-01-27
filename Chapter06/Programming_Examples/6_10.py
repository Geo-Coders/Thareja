# Modify the above program so that it starts counting from the specified location

def count_ch(s,c, beg = 0):
    count = 0
    index = beg
    while index < len(s):
        if s[index]== c:
            count+= 1
    return count
str = input('\n Enter a string : ')
ch = input('\n Enter the character to be searched : ')
count = count_ch(str, ch)
print(f'in {str} {ch} occurs {count} times from begining to end')
loc = int(input('\n from which position do you want to start counting : '))
count = count_ch(str, ch, loc)
print(f'in {str} {ch} occurs{count} times from position {loc} to end')