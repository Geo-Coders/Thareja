# Using dictionary comprehension, create a dictionary of numbers and their
# squares in the range(1-10)

print('--- A Program to implement a Dictionary Comprehesion ---')
print()

def map_nums_to_squares(n):
    return {i: i * i for i in range(n + 1)}
    
print(map_nums_to_squares(100))