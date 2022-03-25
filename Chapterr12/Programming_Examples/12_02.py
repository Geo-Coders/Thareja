# Write a program that opens a file and writes data to it. 
# Handle exceptions that can be generated during the I/O operation

try:
    with open('myFile.txt', 'w') as file:
        file.write('Hello, Good Morning !!!')
except IOError:
    print('Error working with file')
else:
    print('File Writing Successful')
    
            