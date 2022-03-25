# Write a program to combine values in two list using list comprehension
# Combine only those values of a list that are multiples of values in the fist list
print([(x,y) for x in [10,20,30,50] for y in [35,40,55,60] if y % x == 0 or x % y == 0])