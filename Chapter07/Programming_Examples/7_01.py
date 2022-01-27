# Write a program that copies first 10 bytes of a binary file into another
'''
file= open('File.txt', 'wb')
print('Name of the file: ', file.name)
print('File is closed.', file.closed)
print('File is now being close.. You cannot use the File Object')
file.close()
print('File is closed.', file.close())

'''
with open('File1.txt', 'rb') as file1:
    with open('file2.txt', 'wb') as file2:
        buf= file1.read(10)
        file2.write(buf)

print('File Copied')
