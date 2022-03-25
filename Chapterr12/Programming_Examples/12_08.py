# Write a program that randomly generates a number.
# Raise a user-defined exception if the number is below 0.1

import random
class RandomError(Exception):
    pass
try:
    num = random.random()
    if num < 0.1:
        raise RandomError
except RandomError as e:
    print('Random Error Generated ....')
else:
    print('%.3f' %num)