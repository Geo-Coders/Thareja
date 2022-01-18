# Write a program that encrypts a message by adding a key value to every character. (Caesar Cipher)
# Hint: Say, if key= 3, then add 3 to every character

message= 'HelloWorld'
index= 0

while index < len(message):
    letter= message[index]
    print(chr(ord(letter) + 3), end=' ')
    index += 1