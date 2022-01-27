#  Write a program to read an integer number
# Print the reverse of this number using recursion
print('----- The program uses recursion to reverse a number' )
print()
 
def reverse(n,r):
    if n == 0:
        return r
    else:
        return reverse(n//10,r*10 + n%10)
number = int(input('Enter number : '))
reversed_number = reverse(number, 0)
print(f' The reverse of {number} is  {reversed_number}')