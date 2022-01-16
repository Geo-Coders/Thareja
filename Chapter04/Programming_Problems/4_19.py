# Enter two integers as dividend and divisor. If the divisor is greater than zero, 
# then divide the divided by the divisor. Assign their result to an integer variable rem and their quotient
# to a floating point number quo.

print('--- A Program To carry out division ---')
print()

dividend = int(input('Enter the Dividend : '))
divisor = int(input('Enter the Divisor : '))

print()

try:
    rem = (dividend % divisor)
    quo = float(dividend // divisor)

    print(f'The Reminder is : {rem}')
    print(f'The Quotient is : {quo}')
    print()

except ZeroDivisionError:
    print()
    print('The divisor is a zero')
    print()