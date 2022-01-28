# Write a program that converts a list of temperatures in Celsius into Fahrenheit.

def convert_to_F(Temp_C):
    return ((float(9)/5) * Temp_C + 32)

Temp_in_C= (36.5,37,37.5,39)
Temp_in_F= list(map(convert_to_F, Temp_in_C))

print(f'List of temperatures in Celsius : {Temp_in_C}')
print(f'List of temperatures in Fahrenheit : {Temp_in_F}')