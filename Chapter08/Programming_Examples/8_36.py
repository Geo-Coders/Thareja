# Write a program that create a dictionary of radius of a circle and its radius circumference
print('Enter -1 to exit .....')
Circumference ={}
while True:
    r = float(input('Enter radius : '))
    if r == -1:
        break
    else:
        Dict = {r:2*3.14*r}
        Circumference.update(Dict)
print(Circumference)

            
    