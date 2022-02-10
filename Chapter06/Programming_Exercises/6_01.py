# Modify the find_ch() function so that it starts finding the character
# from the specified position in the string.

print('--- A Program to modify find_ch() function ---')
print()

def find_ch(s,c,beg=0):
    index= beg
    while (index < len(s)):
        if s[index] == c:
            print(f'In {str}, \'{c}\' has been found at Index : {index} searching from {beg}')
            return
        else:
            pass
        index += 1
    print(f'{c} is not present in the string')

str= input('Enter a string : ')
ch= input('Enter the character to be searched : ')
print()
find_ch(str,ch)
print()

loc= int(input('From which position do you want to start counting : '))
print()
find_ch(str,ch,loc)
print()