# Write a program that creates two sets-- squares and cubes in range 1-10.
# Demonstrate the use of update(), pop(), remove(), add() and clear() functions.
print()

squares= set([x**2 for x in range(1,10)])
cubes= set([x**3 for x in range(1,10)])

print(f'SQUARES : {squares}')
print(f'CUBES : {cubes}')

squares.update(cubes)

print(F'UPDATE : {squares}')

squares.add(11*11)
squares.add(11*11*11)

print(f'ADD : {squares}')
print(f'POP : {squares.pop()}')

squares.remove(1331)

print(f'REMOVE : {squares}')

squares.clear()

print(f'CLEAR : {squares}')

print()