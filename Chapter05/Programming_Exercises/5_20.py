# write a program to calculate the area of a triangle using function
print('------ A program to get the area of a triangle -----')
print()

def area_of_triangle(base, height):
    area = 0.5* base * height
    return area

base = int(input('Enter the base of a triangle : '))
height = int(input('Enter the height of a triangle : '))
area = area_of_triangle(base, height)
print(f'The area of a triangle is {area}')
    
     