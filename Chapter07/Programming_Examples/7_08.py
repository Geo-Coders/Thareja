# Write a program that reads a file line by line. 
# Each line read from the file is copied to another file wit line numbers specified at the beginning of the line

file1 = open('file1.txt','r')
file2 = open('file.txt','w')
num = 1
for line in file1:
    file2.write(str(num) + ':' + line)
    num +=1
    file1.close()
    file2.close()