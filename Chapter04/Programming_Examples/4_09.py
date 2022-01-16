# Write a program to determine whether the character entered is a vowel or not.
ch= input('Enter any character: ').lower()
if ch in ['a', 'e', 'i', 'o', 'u']: 
    print(f'{ch} is a vowel')
    
print(f'{ch} is a consonant')
