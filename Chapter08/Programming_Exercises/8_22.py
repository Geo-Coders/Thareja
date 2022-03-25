# Write a program that finds the sum of all even numbers in a list
print('----- A program to find sum of all even numbers-----')
print()

num_list = []

even_sum = 0

number = int(input('Enter the total number of list elements : '))

for i in range(1, number +1):
    val  = int(input('Enter the value : '))
    num_list.append(val)
    for j in range(number):
        if num_list[j] % 2 == 0:
            even_sum = even_sum + num_list[j]
    print(even_sum)