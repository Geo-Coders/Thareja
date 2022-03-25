# Make a list of five random numbers
print('----- A list of five random numbers-----')
print()

import random
num_list = []
for i in range(5):
    val = random.randint(1,100)
    num_list.append(val)
print(num_list)
    