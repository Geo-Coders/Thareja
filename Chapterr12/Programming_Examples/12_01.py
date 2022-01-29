# Write a program that prompts the user to enter a number and prints its square.
# if no number is entered(Ctrl+C is pressed), then a KeyboardInterrupt is generated.

num= int(input('Enter the numerator : '))
deno= int(input('Enter the denominator : '))

try:
    quo= num/deno
    print(f'QUOTIENT : {quo}')

except ZeroDivisionError:
    print('Denominator cannot be zero')
    