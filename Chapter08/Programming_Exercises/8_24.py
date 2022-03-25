# Write a program to find whether a particular element is present in the list using a loop
print('----- A program to find an element in the list-----')
print()

shopping = ['Tea', 'Bread', 'Sugar', 'Salt']

is_in_list = input('Enter the name of the item to check : ')

if is_in_list in shopping:
    
    print('The item is in the list')
    
else:
    
    print('Item not in the list')
    