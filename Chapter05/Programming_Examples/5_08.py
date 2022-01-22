# Write a program to calculate the volume of a cuboid using default arguments

def volume(l=4, w=3, h=4):
    print(f'length : {l} \tWidth : {w} \tHeight : {h}')
    return l * w * h
print(f'Volume : {volume(4,6,2)}')
print(f'Volume : {volume(4,6)}')
print(f'Volume : {volume(4)}')
