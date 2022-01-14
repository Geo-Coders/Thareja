# Write a program to find whether the given number is an Amstrong number or not.
# Hint: An Armstrong number of three digits is an integer such that the sum of the cubes of its
# digits is equal to the number itself. For example, 371 is Armstrong number since 3**3 + 7**3 + 1**3 = 371


num= int(input('Enter the number: ')) # take input from the user

sum = 0 # initialize sum

temp = num # find the sum of the cube of each digit
while temp > 0:
    digit_= temp % 10
    sum += digit_ ** 3
    temp //= 10

# display the result
if num == sum:
   print(f'{num} is an Armstrong number')
else:
   print(f"{num} is not an Armstrong number")