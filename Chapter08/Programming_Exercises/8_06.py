# Write a program that uses filter() function to filter out only even numbers from a list

print('----- A list of even numbers using filter()-----')
print()
def is_even(x):
    if x% 2 == 0:
        return x
num_list = [20,5,7,10,15,4,8,6,3,2]
List = []
List = list(filter(is_even, num_list))
print(List)