# Write a program that creates a dictionary of cubes of odd numbers in the range 1-10
Dict = {x:x**3 for x in range(10) if x% 2 == 1}
print(Dict)