# Write a program that reads data from a file and calculates the percentage of vowels and consonants in the file
filename = input('Enter the filename : ')
with open(filename) as file:
    text = file.read()
    count_vowels = 0
    count_consonants = 0
    for  char in text:
        if char in 'aeiou':
            count_vowels +=1
        else:
            count_consonants +=1
print(f'Number of vowels = {count_vowels}')
print(f'Number of consonants = {count_consonants}')
print('Total length of file =', len(text))
print('Percentage of vowels in the file =',((count_vowels)*100)/len(text),'%')
print('Percentage of consonants in the file =',((count_consonants)*100)/len(text),'%')
