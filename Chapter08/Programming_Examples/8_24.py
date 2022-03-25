# Write a program to swap two values using tuple assignment
val1 = 10
val2 = 20
print(f'val1 = {val1} val2 = {val2}')
(val1,val2) = (val2, val1)
print(f'val1 = {val1} val2 = {val2}')