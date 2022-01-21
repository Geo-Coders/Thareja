# Write a program that converts grams to kilograms and meters to centimeters
print('----- A program to convert grams to kilograms and meters to centimeters -----')
print()
grams = float(input('Enter the weight in grams : '))
meters = float(input('Enter length in meters : '))

kilograms = grams / 1000
centimeters = meters * 1000

print(f'The weight in kilograms is {kilograms}')
print(f'The length in centimeters is {centimeters}')

