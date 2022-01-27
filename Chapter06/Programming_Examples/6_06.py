# Write a program that accepts a string from user and redisplays the same string after removing vowels from it

def remove_vowels(s):
    new_str = ''
    for i in s:
        if i in 'aeiouAEIOU':
            pass
        else:
            new_str += i
    print(f'The string without vowels is : {new_str}')
str = input('\n Enter a string : ')
remove_vowels(str)