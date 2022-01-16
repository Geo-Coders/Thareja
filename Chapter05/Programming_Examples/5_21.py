# Write a program to display the date and time using the Time Module

import time

localtime= time.asctime(time.localtime(time.time()))

print()

print(f'Local current time: {localtime}')

print()