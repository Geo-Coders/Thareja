# Write a program that copies first 10 bytes of a binary file into another
with open('File1.txt', 'wb') as file1:
    file1.write('Hello All, hope you are enjoying learning Python.')


with open('File1.txt', 'rb') as file1:
    with open('file2.txt', 'wb') as file2:
        buf= file1.read(10)
        file2.write(buf)

print('File Copied')