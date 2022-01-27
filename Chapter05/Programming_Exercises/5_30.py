# Write a program that converts temperature given in Celsius into Fahrenheit
print('------ A program to convert temperature ------')
print()
def convert(Celsius):
    Fahrenheit = (Celsius * 9/5) + 32
    return Fahrenheit
Celsius = int(input('Enter temperature in Celsius : '))
temp = convert(Celsius)
print(f'Temperature in Fahrenheit is {temp}')

