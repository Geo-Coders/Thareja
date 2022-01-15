# Write a program that  prompts users to enter numbers. 
# Once the user enters -1, it displays the count, sum and 
# average of even numbers and that of odd numbers.


print('--- A Program evaluate the even numbers and odd numbers entered by the user ---')
print()
print('Enter -1 to quit the Program')
print()

even_counter= odd_counter= even_sum= odd_sum= odd_average= 0

input_num= int(input('Enter to evaluate: '))
while input_num != -1:
    if input_num % 2 == 0:
        even_counter += 1
        even_sum += input_num
        even_average = even_sum/even_counter

    else:
        odd_counter += 1
        odd_sum += input_num
        odd_average = odd_sum/odd_counter

    input_num= int(input('Enter another number: '))

print()
print(f'The even number count is {even_counter}')
print(f'The even number sum is {even_sum}')
print(f'The even number averag is {even_average}')
print()
print(f'The odd number count is {odd_counter}')
print(f'The odd number sum is {odd_sum}')
print(f'The odd number averag is {odd_average}')





