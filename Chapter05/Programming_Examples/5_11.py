# Write a program that uses docstrings and variable-length arguments to add
# the value passed to the function.

def add(*args):
    """ Function returns the sum of values passed to it """
    sum= 0
    for i in args:
        sum += 1
    return sum

print(add.__doc__)
print()
print(f'SUM = {add(25,30,45,50)}')
print()









