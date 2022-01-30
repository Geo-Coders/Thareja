# Write a program that copies one Python script into another
# In such a ay that all comment lines are skipped and not copied in the destination file

with open('First.py','rb') as file1:
    with open('second.py', 'wb') as file2:
        while True:
            buf = file1.readline()
            if len(buf) !=0:
                if(buf[0]) =='#':
                    continue
                else:
                    file2.write(buf)
            else:
                break
print('File Copied')
                    