# Write a program to calculate roots of a quadritic equation

a= int(input('Enter the values of a: '))
b= int(input('Enter the values of a: '))
c= int(input('Enter the values of a: '))

D= (b*b)- (4 * a * c)
deno = 2*a
if D > 0:
    print('Real Roots')
    root1= (-b + D**0.5)/deno
    root2= (-b + D**0.5)/deno
    print(f'Root1= {root1} \tRoot2= {root2}')

elif D == 0:
    print('Equal Roots')
    root1=-b/deno
    print(f'Root1 and Root2 = {root1}')

print('Imaginary Roots')
