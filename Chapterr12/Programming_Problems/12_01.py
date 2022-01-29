# Write a program that finds smaller of two given numbers.
# if the first number is smaller than the second, then 
# generate an Assertion error.

print('--- A Program to find a smaller of two given numbers ---')
print()

try:
    num = int(input('Enter the first number : '))
    num0 = int(input('Enter the second number : '))

    if num > num0:
        raise AssertionError

except AssertionError:
    print('Assertion Error has been caught!')

else:
    print('Have a good day!')

print()