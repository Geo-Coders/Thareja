# Write a program using filter function to a list of squares of numbers from 1-10
# Then use the for... in construct to sum the elements in the generated list

def square(x):
    return (x**2)
squares = []
squares  =  list(filter(square, range(1, 11)))
print(f'List of squares in the range 1-10 = {squares}')
sum = 0
for i in squares:
    sum +=i
print(f'Sum of squares in the range 1-10 = {sum}')