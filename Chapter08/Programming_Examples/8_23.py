# Write a program to calculate distance between two points.

import math

p1= []
p2= []
x1= int(input('Enter the x co-ordinate of starting point: '))
y1= int(input('Enter the y co-ordinate of starting point: '))
x2= int(input('Enter the x co-ordinate of ending point : '))
y2= int(input('Enter the y co-ordinate of ending point : '))

p1.append(x1)
p1.append(x2)
p2.append(y1)
p2.append(y2)

distance= math.sqrt( ((p1[0]-p2[0])**2) + ((p1[1] - p2[1])**2) )

print(f'DISTANCE = {round(distance,2)}')