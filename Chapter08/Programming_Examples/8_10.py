# Write a program that creates a list of 10 random integers
# Then create two lists - Odd List and Even List
# that has all odd and even values in the list respectively

import random

num_list = []

for i in range(10):
    val = random.randint(1,100)
    num_list.append(val)
    
print(f'Original List : {num_list}')

even_list = []
odd_list = []

for i in range(len(num_list)):
    if(num_list[i] % 2 == 0):
        even_list.append(num_list[i])
    else:
        odd_list.append(num_list[i])
        
print(f'Even Numbers List = {even_list}')

print(f'Odd Numbers List = {odd_list}')
