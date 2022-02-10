# Modify the find_ch() function so that it starts finding the character
# from the specified position in the string.

print('--- A Program to modify find_ch() function ---')
print()

def find_ch(s,c):
    index= 0
    while (index < len(s)):
        if s[index] == c:
            print(f'{c} found in string at Index : {index}')
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