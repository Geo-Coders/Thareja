# Modify the above program to calculate the parking charges. 
# Read the hours and minutes when the vehicle enters the parking lot.
# When the vehicle is leaving, enter its leaving time.
# Calculate the difference between the two timings to calculate
# the number of hours and minutes for which the vehicle was parked
# Finally, calculate the charges based on following rules and 
# display the result on the screen.

print (' *****\tA PROGRAM TO CALCULATE PARKING CHARGES OF A VEHICLE\t***** ')
print ('*' * 100)
print ('\tChoose the type of a vehicle you have by pressing the corresponding number.')

cond = True
type = 0

while cond:   
    flag = 0
    if type in [1,2,3]:
        cond = False
    if type > 3:
        print ('The type of vehicle selected is not supported')
        choice = input ('\nWould you wish to continue? (y/n) \n\t>>> ')
       
        if choice.lower() != 'y':
            flag = 1 
            break
        else:
            type = 0
    else:
       
        if type not in [1,2,3]:
            type = int (input ('\t1.cars \n\t2.Truck/bus. \n\t3.Scooter/Cycle/Motor cycle.\n>>> '))
        
else:
    in_hrs = int(input('Enter the time of entrace (HH) : '))
    in_min = int(input('Enter the time of entrace (MM) : '))
    out_hrs = int(input('Enter the time of Leaving (HH) : '))
    out_min = int(input('Enter the time of leaving (MM) : '))

    time_spent = (out_hrs + (out_min/60)) - (in_hrs + (in_min/60))

    if time_spent <= 3:
            if flag == 0:
                if type == 1:
                    print(f'Your charges are : {time_spent * 10} £.')
                elif type == 2:
                    print(f'Your charges are : {time_spent * 20} £.')
                elif type == 3:
                    print(f'Your charges are : {time_spent * 5} £.')
    elif time_spent > 3:
            if type == 1:
                print(f'Your charges are : {time_spent * 20} £.')
            elif type == 2:
                print(f'Your charges are : {time_spent * 30} £.')
            elif type == 3:
                print(f'Your charges are : {time_spent * 10} £.')
    else:
        print('The type of Vehicyle selected is not supported')


print('*' * 100)



