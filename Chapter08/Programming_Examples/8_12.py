# Write a program that passes a list to a function that scales each element in the list by a factor of 10
#  Print the list values at different stages to show that 
# changes made to one list automatically reflected in the other list
def change(list1):
    
    for i in range(len(list1)):
        
        list1[i] = list1[i] * 10
        
    print(f'After change in function, list is : {list1}')
    
num_list = [1,2,3,4,5,6]

print(f'Original List is : {num_list}')

change(num_list)

print(f'List after change is {num_list}')
