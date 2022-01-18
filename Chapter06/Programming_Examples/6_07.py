# Write a program that finds whether a given character is present in a string or not
# In case it is present it prints the index at which it is present.
# Do not use built-in find functions to search the character.

def find_ch(s,c):
    index= 0
    while index < len(s):
        if s[index] == c:
            print(f'{c} found in string at index {index}')
            return
        else:
            pass
        index += 1

    print(f'{c} is not present in the string')

str= input('Enter a string : ')
ch= input('Enter the character to be searched : ')

find_ch(str,ch)

print()