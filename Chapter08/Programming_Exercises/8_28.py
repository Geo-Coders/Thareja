# Write a program that prompts a number from user and adds it in a list
#   If the value entered by the user is greater than 100, then add 'EXCESS' in the list

list = []
n = int(input('Enter the number of elements : '))
for i in range(0,n):
    element = int(input())
    if element >= 100:
        list.append('EXCESS')
    else:
        
        list.append(element)
        print(list)