# Write a program to create a list of numbers in the specified range in particular
# steps. Reverse the list and print its values.

num_list= []
m= int(input('Enter the starting of the range: '))
n= int(input('Enter the ending of the range: '))
o= int(input('Enter the steps in the range: '))

for i in range(m,n,o):
    num_list.append(i)

print(f'Original List : {num_list}')
num_list.reverse()
print(f'Reverse List : {num_list}')