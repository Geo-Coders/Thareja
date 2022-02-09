# Write a program that has a predefined list. Create a copy of this list in such
# a way that only those values that are in valid_tuple are added in the new list.

print('--- A Program with a Predefined list ---')
print()

list_= ['a','b','c','d','e','f','g','h','i','j','k','l','m']
valid_tuple= ['a','c','d','e','h','j','l']
new_list= []

for item in list_:
    if item in valid_tuple:
        new_list.append(item)
        print(f'{item} has been added')
    else:
        print(f'{item} has been skipped')

print()
print(f'The New List is {new_list}')
print()


