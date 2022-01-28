# Write a program using a function that returns the area and circumference of a
# circle whose radius is passed as an argument.

PI= 3.14
def cal_a_r(r):
    return  (PI*r*r, 2*PI*r)

radius= float(input('Enter the radius : '))
(area, circumference) = cal_a_r(radius)

print(f'Area of the circle with radius {radius} = {area}')
print(f'Circumference of the Circle with radius {radius} = {circumference}')

