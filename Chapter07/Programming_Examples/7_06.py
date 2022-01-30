# Write a program that computes the total size of all files in C:\Python34 folder

import os
totalSize = 0
for file in os.listdir('C:\Python34'):
    totalSize += os.path.getsize(os.path.join('C:\Python34', file))
    print(f'Total size of all files in C:\Python34 = {totalSize}')