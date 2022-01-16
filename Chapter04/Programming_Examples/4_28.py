# Write a program using a while loop that asks the user for a number, and prints a countdown from that number to zero

n = int(input('Enter the value of n : '))
while n > 0:
    print(n, end =' ')
    n -= 1