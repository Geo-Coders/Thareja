# Write a program that creates a list of numbers from 1-20 that are either
# divisible by 2 or divisible by 4 without using the filter function

div_2_4= []
for i in range(2,22):
    if i % 2 == 0 or i % 4 == 0:
        div_2_4.append(i)

print(div_2_4)