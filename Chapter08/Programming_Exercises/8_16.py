# Write a program to remove duplicates from a dictionary
print('----- A program to remove duplicates-----')
print()

num_list = [1,2,3,4,5,6,7,6,5,4]
print(f'Original list : {num_list}')
i = 0
while i<len(num_list):
    num = num_list[i]
    for j in range(i + 1, len(num_list)):
        val = num_list[j]
        if val == num:
            num_list.pop(j)
    i = i + 1
print(f'List after removing duplicates : {num_list}')
            