# Write a program using map() function to create a list of squares of numbers
# in the range 1-10

from pip import List


def squares(x):
    return x*x


sq_list= list(map(squares, range(1,11)))

print(f'Positive Values List = {sq_list}')