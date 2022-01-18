# Write a program that counts the occurrences of a character in a string.
# Do not use built-in count function

def count_ch(s,c):
    count= 0
    for i in s:
        if i == c:
            count += 1
    return count

str= input('Enter a string: ')
ch= input('Enter the character to be searched: ')

print()

count= count_ch(str, ch)

print(f'In {str} {ch} occurs {count} times')

print()