# Write a program to calculate parking charges of a vehicle.
# Enter the type of vehicle as a character (Like c for car, b for bus,etc)
# And number of hours, then calculate charges as given below
# Truck/bus - $20 per hour
# car - $10 per hour
# scooter/cycle/motor cycle - $5 per hour

input_ = input('Enter the type of the car ( b, t, c, s) : ')
Time = int(input('Enter the number of hours parked : '))

if input_ == 'b' or input_ =='t':
    charges = Time * 20
elif input_ == 'c':
    charges = Time * 10
    
else:
    charges = Time * 5
print(f'Your parking fee is ${charges}')