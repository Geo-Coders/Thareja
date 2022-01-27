# Write a program that accepts filename as an input from the user. Open the file 
# and count the number of times a character appears in the file.


filename= input('Enter the filename: ')
with open(filename) as file:
    text= file.read()
    letter= input('Enter the character to be searched: ')
    count= 0
    for char in text:
        if char == letter:
            count += 1

print(f'{letter} appears {count} times in file')







