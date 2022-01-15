# Write a Program to display the cos(x) and tan(x) value where
# x ranges from 0 to 360 in steps of 15

import math

print('--- A Program to display the cos(x) and tan(x) ---')
print()

for x in range(0,360,15):
    print(f'Cos of {x}: {round(math.cos(x),2)}')
    
    print(f'Tan of {x}: {round(math.tan(x),2)}')
    print()
