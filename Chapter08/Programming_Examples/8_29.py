# Write a program that accepts different number of arguments and 
# return sum of only the positive values passed to it.

def sum_pos(*args):
    tot= 0
    for i in args:
        if i > 0:
            tot += 1

    return tot

print(f'sum_pos(1,-9,2,-8,3,-7,4,-6,5) = {sum_pos(1,-9,2,-8,3,-7,4,-6,5)}')