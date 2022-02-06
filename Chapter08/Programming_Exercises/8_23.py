# Write a program that reverse a list using a loop

print('--- A Program to reverse a list using a loop ---')
print()

list_= [1,2,3,4,5,6,7,8,9,10]
reversed_list= list()

for i in list_:
    reversed_list.insert(-i,i)

print(f'The Reversed list is : {reversed_list}')

print()
