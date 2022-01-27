# Write a program to print index at which a particular value exists.
# if the value exists at multiple locations in the list, then print all the indices.
# Also, count the number of times that value is repeated in the list

num_list= [1,2,3,4,5,6,5,4,3,2,1]
num= int(input('Enter the value to be searched : '))
i= 0
count= 0
while i < len(num_list):
    if num == num_list[i]:
        print(f'{num} found at location {i}')
        count += 1
    i += 1

print(f'{num} appears {count} times in the list')



