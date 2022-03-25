# Write a program using filter function to a list of cubes of numbers from 1-10


def cube(x):
    return x **3


cubes = list(map(cube, range(1,11)))

print(cubes)