# Write a Program using a function that returns the surface area and volume of a sphere.
import math

print('--- A Program to return the surface area and volume of a sphere ---')
print()

def surface_area(radius):
    ''' A function that take the radius then returns the surface area of a sphere.'''
    return (4 * math.pi * (radius**2))

def volume(radius):
    ''' A function that take the radius then returns the volume of a sphere.'''
    return ((4/3) * math.pi * (radius**3))

def main():
    ''' A function that contains the main program '''
    radius_= int(input('Enter the radius of a sphere: '))
    print()
    print(f'The Surface Area of the sphere with radius {radius_} is {round(surface_area(radius_),2)}')
    print(f'The volume of sphere with radius {radius_} is {round(volume(radius_),2)}')
    print()

if __name__ == '__main__':
    main()
