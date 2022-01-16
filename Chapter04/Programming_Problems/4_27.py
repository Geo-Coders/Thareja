# Write a Program to read an angle from the user and then displays its quadrant

print('--- A Program to display the quadrant of an angle from the user ---')
print()

prompt_angle = int(input('Enter an Angle between 0 - 360, or press -1 to quit : '))
while True:
    flag = 0
    if prompt_angle == -1:
        flag = 1
        print()
        print('Thank you for trying, See you Tomorrow!')
        break
    if flag == 0:
        if prompt_angle >= 0 and prompt_angle <= 90:
            print(f' The Angle {prompt_angle} is in First Quadrant.')

        elif prompt_angle > 90 and prompt_angle <= 180:
            print(f' The Angle {prompt_angle} is in Second Quadrant.')

        elif prompt_angle > 180 and prompt_angle <= 270:
            print(f' The Angle {prompt_angle} is in Third Quadrant.')

        elif prompt_angle > 270  and prompt_angle <= 360:
            print(f' The Angle {prompt_angle} is in Forth Quadrant.')

        else:
            print('Enter a valid angle')

    print()
    prompt_angle= int(input(' Enter another Angle between 0 - 360: '))
    



